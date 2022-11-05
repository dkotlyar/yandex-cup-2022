SELECT cast(AVG(delay_ms) as numeric) as avg_network_time_ms
FROM (
WITH RECURSIVE r1 AS (
    SELECT
        receiver.datetime - sender.datetime as delay,
        sender.request_id as base_req_id,
        sender.type, sender.host, sender.data
    FROM requests sender
    JOIN requests receiver on sender.request_id = receiver.parent_request_id
    WHERE (
        sender.type = 'RequestSent'
        AND receiver.type = 'RequestReceived'
        AND receiver.host = sender.data
        AND sender.parent_request_id isnull
    )

    UNION ALL

    SELECT
        receiver.datetime - sender.datetime as delay,
        r1.base_req_id,
        sender.type, sender.host, sender.data
    FROM requests sender
    JOIN requests receiver on sender.request_id = receiver.parent_request_id
    JOIN r1 ON r1.base_req_id = sender.parent_request_id
    WHERE (
        sender.type = 'RequestSent'
        AND receiver.type = 'RequestReceived'
        AND receiver.host = sender.data
        AND r1.type = 'RequestSent'
        AND r1.data = sender.host
    )

),
r2 AS (
    SELECT
        receiver.datetime - sender.datetime as delay,
        receiver.request_id as base_req_id,
        receiver.type, receiver.host, receiver.data
    FROM requests receiver
    JOIN requests sender on sender.parent_request_id = receiver.request_id
    WHERE (
        sender.type = 'ResponseSent'
        AND receiver.type = 'ResponseReceived'
        AND receiver.data LIKE sender.host || '%'
        AND receiver.parent_request_id isnull
    )

    UNION ALL

    SELECT
        receiver.datetime - sender.datetime as delay,
        r2.base_req_id,
        receiver.type, receiver.host, receiver.data
    FROM Requests receiver
    JOIN requests sender on sender.parent_request_id = receiver.request_id
    JOIN r2 ON r2.base_req_id = receiver.parent_request_id
    WHERE (
        sender.type = 'ResponseSent'
        AND receiver.type = 'ResponseReceived'
        AND receiver.data LIKE sender.host || '%'
        AND r2.type = 'ResponseReceived'
        AND r2.data LIKE receiver.host || '%'
    )

),
j AS (
    SELECT delay, base_req_id
    FROM r1
    UNION ALL
    SELECT delay, base_req_id
    FROM r2
)
SELECT sum(EXTRACT(epoch FROM delay)) * 1000 as delay_ms
FROM j
GROUP BY base_req_id
) as req_delays