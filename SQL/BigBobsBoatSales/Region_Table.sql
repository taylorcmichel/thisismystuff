CREATE TABLE Region_Table (
	Region_ID 	varchar(2) 	PRIMARY KEY 	NOT NULL,
	Region 		varchar(10) 			NOT NULL
);

INSERT INTO Region_Table
	(Region_ID, Region)
VALUES
	('R1', 'West'		),
	('R2', 'Midwest'	),
	('R3', 'South'		),
	('R4', 'Northeast'	);

SELECT *
FROM Region_Table
