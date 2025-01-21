SELECT 
    Date,
    [Close],
    LAG([Close], 1) OVER (ORDER BY Date) AS Previous_Close,
    (([Close] - LAG([Close], 1) OVER (ORDER BY Date)) / LAG([Close], 1) OVER (ORDER BY Date)) * 100 AS Daily_Return
FROM NVIDIA_STOCK
ORDER BY Date;