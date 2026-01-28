def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    is_triangle = (
        ( (triangle['x'] + triangle['y']) > triangle['z'] ) &
        ( (triangle['x'] + triangle['z']) > triangle['y'] ) &
        ( (triangle['y'] + triangle['z']) > triangle['x'] )
    )
    triangle = (
        triangle
        .assign(triangle=is_triangle.map({True: 'Yes', False: 'No'}))
    )
    return triangle

