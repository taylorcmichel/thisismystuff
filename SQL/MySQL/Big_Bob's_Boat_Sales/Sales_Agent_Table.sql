CREATE TABLE Sales_Agent_Table (
	Sales_Agent_ID 		varchar(3)	  NOT NULL,
	Sales_Agent_Name 	varchar(20)	  NOT NULL,
  PRIMARY KEY (Sales_Agent_ID)
);

INSERT INTO Sales_Agent_Table (
	Sales_Agent_ID,
	Sales_Agent_Name
)
VALUES
	('473','David'		),
	('474','Ezekiel'	),
	('475','Thomas'		),
	('476','Elizabeth'),
	('477','Jaime'		),
	('478','Chris'		),
	('479','Taylor'		),
	('480','Stew'		  ),
	('481','Candace'	),
	('482','TJ'			  ),
	('483','Jose'		  ),
	('484','Stephen'	),
	('485','Louanne'	),
	('486','John'	  	),
	('487','Louis'		),
	('488','Ronnie'		),
	('489','Ethan'		),
	('490','Roule'		),
	('491','Jade'		  ),
	('492','Maddy'		),
	('493','Simeon'		),
	('494','Randy'		),
	('495','Jason'		),
	('496','Johnny'		),
	('497','Brad'		  ),
	('498','Angie'		),
	('499','Ryan'		  ),
	('500','Jacob'		),
	('501','Jase'	  	);

SELECT *
FROM Sales_Agent_Table
