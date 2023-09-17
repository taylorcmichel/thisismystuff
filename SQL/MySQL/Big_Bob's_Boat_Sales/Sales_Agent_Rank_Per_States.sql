SELECT
	  DISTINCT(Sales_Agent_Name),
    Qty_Sold,
    Principle_State,
    DENSE_RANK() OVER(PARTITION BY Principle_State ORDER BY Qty_Sold DESC) AS Qty_Sold_Rank
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
WHERE Principle_State = 'Connecticut';
