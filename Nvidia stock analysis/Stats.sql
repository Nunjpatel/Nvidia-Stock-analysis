SELECT 
    AVG([Close]) AS 'Average Close',
    MIN([Close]) AS 'Min Close',
    MAX([Close]) AS 'Max Close',
    STDEV([Close]) AS 'Std Dev of Close'
FROM NVIDIA_STOCK;