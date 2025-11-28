def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world.loc[(world['area'] >= 3000000) | (world['population'] >= 25000000), ['name', 'population', 'area']]

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    filtered_countires = (
        world
        .query("area >= 3000000 | population >= 25000000")
        .loc[:, ['name', 'population', 'area']]
    )
    return filtered_countires