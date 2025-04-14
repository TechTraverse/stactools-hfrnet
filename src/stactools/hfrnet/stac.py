from datetime import datetime, timezone

import xarray
from pydantic import BaseModel
from pystac import (
    Collection,
    Extent,
    Item,
    SpatialExtent,
    TemporalExtent,
)

import stactools.core.create


def create_collection() -> Collection:
    """Creates a STAC Collection.

    This function should create a collection for this dataset. See `the STAC
    specification
    <https://github.com/radiantearth/stac-spec/blob/master/collection-spec/collection-spec.md>`_
    for information about collection fields, and
    `Collection<https://pystac.readthedocs.io/en/latest/api.html#collection>`_
    for information about the PySTAC class.

    Returns:
        Collection: STAC Collection object
    """
    extent = Extent(
        SpatialExtent([[-180.0, -90.0, 180.0, 90.0]]),
        TemporalExtent([[datetime.now(tz=timezone.utc), None]]),
    )

    collection = Collection(
        id="hfrnet-collection",
        title="Near-Real Time Surface Ocean Velocity, U.S. West Coast, 500m Resolution",
        description="""
            Surface ocean velocities estimated from HF-Radar are representative 
            of the upper 0.3 meters of the ocean.  The main objective of 
            near-real time processing is to produce the best product from 
            available data at the time of processing.  Radial velocity 
            measurements are obtained from individual radar sites through the 
            U.S. HF-Radar Network. Hourly radial data are processed by unweighted 
            least squares on a 500m resolution grid of the U.S. West Coast to 
            produce near real-time surface current maps.
            instrument: Earth Remote Sensing Instruments, Active Remote Sensing, 
            Profilers/Sounders, Radar Sounders, Doppler RADAR
        """,
        extent=extent,
        extra_fields={
            "keywords": [
                "Earth Science",
                "Oceans",
                "Coastal Processes",
                "Marine Environment Monitoring",
                "Ocean Circulation",
                "Ocean Currents",
                "Surface Currents",
                "Wind-Driven Circulation",
                "Tides",
                "Tidal Currents",
            ],
            "processing_level": (
                "Near real-time dataset with automated data acquisition and "
                "processing quality control",
            ),
        },
    )
    return collection


class HorizontalSpatialDimension(BaseModel):
    pass


class VerticalSpatialDimension(BaseModel):
    pass


class TemporalDimension(BaseModel):
    type: str
    description: str
    extent: str | None
    values: list[str]
    step: str | None


class SpatialVectorDimension(BaseModel):
    pass


class AdditionalDimension(BaseModel):
    pass


Dimension = (
    HorizontalSpatialDimension
    | VerticalSpatialDimension
    | TemporalDimension
    | SpatialVectorDimension
    | AdditionalDimension
)


class VariableObject(BaseModel):
    dimensions: list[str]
    type: str
    description: str
    extent: list[int | str | None]
    values: list[int | str]
    unit: str


def create_item(asset_href: str) -> Item:
    """Creates a STAC item from a raster asset.

    This example function uses :py:func:`stactools.core.utils.create_item` to
    generate an example item.  Datasets should customize the item with
    dataset-specific information, e.g.  extracted from metadata files.

    See `the STAC specification
    <https://github.com/radiantearth/stac-spec/blob/master/item-spec/item-spec.md>`_
    for information about an item's fields, and
    `Item<https://pystac.readthedocs.io/en/latest/api/pystac.html#pystac.Item>`_ for
    information on the PySTAC class.

    This function should be updated to take all hrefs needed to build the item.
    It is an anti-pattern to assume that related files (e.g. metadata) are in
    the same directory as the primary file.

    Args:
        asset_href (str): The HREF pointing to an asset associated with the item

    Returns:
        Item: STAC Item object
    """
    item = stactools.core.create.item(asset_href)
    item.id = asset_href  # FIXME: revisit - better to not have slashes

    ds: xarray.Dataset = xarray.Dataset()
    min_epoch_seconds: int = int(ds["time"].min().item() / 1_000_000_000)
    max_epoch_seconds: int = int(ds["time"].max().item() / 1_000_000_000)

    item.properties["cube:dimensions"] = {
        "time": TemporalDimension(
            type="temporal",
            description="",
            extent=None,
            values=[],
            step=None,
        ),
        # "lat": VariableObject(dimensions=[], type="data"),
        # "lon",
    }
    item.properties["cube:variables"] = {
        "time": VariableObject(
            dimensions=["time"],
            # TODO: validate. It's not auxiliary because it is in cub:dimensions?
            type="data",
            description="seconds since 1970-01-01",
            extent=[min_epoch_seconds, max_epoch_seconds],
            values=[],
            unit="second",
        ),
        # "lat": VariableObject(dimensions=[], type="data"),
        # "lon",
        # "time_bnds",
        # "depth",
        # "depth_bnds",
        # "wgs84",
        # "u_mean",
        # "v_mean",
        # "u_var",
        # "v_var",
        # "u_min",
        # "v_min",
        # "u_max",
        # "v_max",
        # "n_obs",
        # "processing_parameters",
    }
    item.properties["custom_attribute"] = "foo"
    return item
