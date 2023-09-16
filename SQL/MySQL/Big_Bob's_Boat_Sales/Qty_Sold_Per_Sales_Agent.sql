-- Use DISTINCT combined with a Windows Function in order to extract
-- a list of qty of boats sold per sales agents and display them in
-- descending order.

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
ORDER BY Qty_Sold DESC
