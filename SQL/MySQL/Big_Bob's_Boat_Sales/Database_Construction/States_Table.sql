CREATE TABLE States_Table (
	Location_ID		varchar(3)	NOT NULL,
	Region_ID		varchar(2)	NOT NULL,
	Principle_State 	varchar(15)	NOT NULL,
  PRIMARY KEY (Location_ID),
  FOREIGN KEY (Region_ID)			REFERENCES Region_Table(Region_ID)
);

INSERT INTO States_Table (
	Location_ID,
	Region_ID,
	Principle_State
)
VALUES
	('L1', 	'R1', 'Washington'		),
	('L2', 	'R1', 'Oregon'		  	),
	('L3', 	'R1', 'California'		),
	('L4', 	'R1', 'Idaho'			),
	('L5', 	'R1', 'Nevada'		  	),
	('L6', 	'R1', 'Utah'			),
	('L7', 	'R1', 'Arizona'		  	),
	('L8', 	'R1', 'Montana'			),
	('L9', 	'R1', 'Wyoming'		  	),
	('L10', 'R1', 'Colorado'	  	),
	('L11', 'R1', 'New Mexico'		),
	('L12', 'R1', 'Alaska'		  	),
	('L13', 'R1', 'Hawaii'		  	),
	('L14', 'R2', 'North Dakota'		),
	('L15', 'R2', 'South Dakota'		),
	('L16', 'R2', 'Nebraska'		),
	('L17', 'R2', 'Kansas'			),
	('L18', 'R2', 'Minnesota'	  	),
	('L19', 'R2', 'Iowa'			),
	('L20', 'R2', 'Missouri'		),
	('L21', 'R2', 'Wisconsin'		),
	('L22', 'R2', 'Illinois'		),
	('L23', 'R2', 'Michigan'		),
	('L24', 'R2', 'Indiana'			),
	('L25', 'R2', 'Ohio'			),
	('L26', 'R3', 'Oklahoma'	  	),
	('L27', 'R3', 'Texas'			),
	('L28', 'R3', 'Arkansas'	  	),
	('L29', 'R3', 'Louisana'		),
	('L30', 'R3', 'Kentucky'		),
	('L31', 'R3', 'Tennessee'		),
	('L32', 'R3', 'Mississippi'		),
	('L33', 'R3', 'Alabama'			),
	('L34', 'R3', 'West Virginia'		),
	('L35', 'R3', 'Maryland'	  	),
  	('L36', 'R3', 'Virginia'		),
	('L37', 'R3', 'North Carolina'		),
	('L38', 'R3', 'South Carolina'		),
	('L39', 'R3', 'Georgia'			),
	('L40', 'R3', 'Florida'		  	),
	('L41', 'R4', 'Maine'			),
	('L42', 'R4', 'Vermont'		  	),
	('L43', 'R4', 'New Hampshire'		),
	('L44', 'R4', 'Massachusetts'		),
	('L45', 'R4', 'Rhode Island'		),
	('L46', 'R4', 'Connecticut'		),
	('L47', 'R4', 'New York'		),
	('L48', 'R4', 'New Jersey'		),
	('L49', 'R4', 'Pennsylvania'		),
	('L50', 'R4', 'Delaware'		);

SELECT *
FROM States_Table
