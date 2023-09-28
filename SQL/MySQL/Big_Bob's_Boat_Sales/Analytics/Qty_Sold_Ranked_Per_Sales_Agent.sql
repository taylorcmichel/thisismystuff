WITH cte_Total_Sold_Per_Sales_Agent (
  Sales_Agent_Name,
  Qty_Sold
)
AS (
	SELECT
    DISTINCT(Sales_Agent_Name),
		SUM(Qty_Sold) OVER(PARTITION BY Sales_Agent_Name) AS Qty_Sold
	FROM Orders_Table a
	INNER JOIN Products_Table b
	ON (
		a.Product_Code = b.Product_Code
	)
	INNER JOIN Sales_Agent_Table c
	ON (
		a.Sales_Agent_ID = c.Sales_Agent_ID
	)
	INNER JOIN States_Table d
	ON (
		a.State_ID = d.Location_ID
	)
	ORDER BY Qty_Sold DESC
)

SELECT 
  Sales_Agent_Name,
  Qty_Sold,
  DENSE_RANK() OVER(ORDER BY Qty_Sold DESC) AS Total_Sales_Revenue_Rank
FROM cte_Total_Sold_Per_Sales_Agent LIMIT 10;
