SELECT DISTINCT(id)
FROM (SELECT id
      FROM (SELECT id,
                   GREATEST(Ax, Cx) <= LEAST(Bx, Dx) AND GREATEST(Ay, Cy) <= LEAST(By, Dy) AND
                   ((Bx - Ax) * (Cy - Ay) - (By - Ay) * (Cx - Ax)) *
                   ((Bx - Ax) * (Dy - Ay) - (By - Ay) * (Dx - Ax)) <= 0 AND
                   ((Dx - Cx) * (Ay - Cy) - (Dy - Cy) * (Ax - Cx)) *
                   ((Dx - Cx) * (By - Cy) - (Dy - Cy) * (Bx - Cx)) <= 0 as intersects
            FROM (SELECT id,
                         cast(LEAST(begin_x, end_x) as BIGINT)    as Ax,
                         cast(LEAST(begin_y, end_y) as BIGINT)    as Ay,
                         cast(GREATEST(begin_x, end_x) as BIGINT) as Bx,
                         cast(GREATEST(begin_y, end_y) as BIGINT) as By,
                         _X_LEFT_                      as Cx,
                         _Y_BOTTOM_                      as Cy,
                         _X_RIGHT_                      as Dx,
                         _Y_TOP_                      as Dy
                  FROM (SELECT id, begin_x, begin_y, end_x, end_y FROM lines UNION SELECT id, begin_x, begin_y, end_x, end_y FROM polygons) as g4
                  UNION ALL
                  SELECT id,
                         cast(LEAST(begin_x, end_x) as BIGINT)    as Ax,
                         cast(LEAST(begin_y, end_y) as BIGINT)    as Ay,
                         cast(GREATEST(begin_x, end_x) as BIGINT) as Bx,
                         cast(GREATEST(begin_y, end_y) as BIGINT) as By,
                         _X_RIGHT_                      as Cx,
                         _Y_BOTTOM_                      as Cy,
                         _X_LEFT_                      as Dx,
                         _Y_TOP_                      as Dy
                  FROM (SELECT id, begin_x, begin_y, end_x, end_y FROM lines UNION SELECT id, begin_x, begin_y, end_x, end_y FROM polygons) as g4) as g) as g2
      WHERE g2.intersects
      UNION
      SELECT objects.id
      FROM objects
      LEFT JOIN points p on objects.id = p.id
      LEFT JOIN lines l on objects.id = l.id
      LEFT JOIN polygons pg on objects.id = pg.id
      WHERE
            p.x <= _X_RIGHT_ AND p.x >= _X_LEFT_ AND
            p.y <= _Y_TOP_ AND p.y >= _Y_BOTTOM_ OR
            l.begin_x <= _X_RIGHT_ AND l.begin_x >= _X_LEFT_ AND
            l.begin_y <= _Y_TOP_ AND l.begin_y >= _Y_BOTTOM_ OR
            l.end_x <= _X_RIGHT_ AND l.end_x >= _X_LEFT_ AND
            l.end_y <= _Y_TOP_ AND l.end_y >= _Y_BOTTOM_ OR
            pg.begin_x <= _X_RIGHT_ AND pg.begin_x >= _X_LEFT_ AND
            pg.begin_y <= _Y_TOP_ AND pg.begin_y >= _Y_BOTTOM_ OR
            pg.end_x <= _X_RIGHT_ AND pg.end_x >= _X_LEFT_ AND
            pg.end_y <= _Y_TOP_ AND pg.end_y >= _Y_BOTTOM_
) as g3
;