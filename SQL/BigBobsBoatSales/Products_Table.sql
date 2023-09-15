CREATE TABLE Products_Table (
	Product_Code 				varchar(10) 	PRIMARY KEY 	NOT NULL,
	Boat_Model_Name 			varchar(50) 			NOT NULL,
	Boat_Length_Feet 			varchar(3) 			NOT NULL,
	Manufacturing_and_Inventory_Cost 	money 				NOT NULL,
	Retail_Price 				money 				NOT NULL
);

INSERT INTO Products_Table (
	Product_Code, Boat_Model_Name, Boat_Length_Feet, Manufacturing_and_Inventory_Cost,
	Retail_Price)
VALUES 
	('BT_1001', 'Gulf Regular',		'70', '102856', '166348'),
	('BT_1002', 'Ocean View',		'72', '207222', '270984'),
	('BT_1003', 'Turkey Cult Club',		'70', '341505', '388056'),
	('BT_1004', 'Ace of Clubs Pro',		'73', '329026', '375220'),
	('BT_1005', 'Bow Midwestern',		'74', '251021', '404774'),
	('BT_1006', 'Ballroom Triage',		'73', '239200', '308911'),
	('BT_1007', 'View From The Moon',	'78', '405391', '465784'),
	('BT_1008', 'Ace of Spades Pro',	'73', '244248', '295107'),
	('BT_1009', 'Gulf Club',		'73', '159519', '214539'),
	('BT_1010', 'Travelling Blues',		'74', '285592', '348844'),
	('BT_1011', 'Prevailing Winds',		'75', '225335', '293348'),
	('BT_1012', 'When In Dubai',		'76', '324198', '392676'),
	('BT_1013', 'Turbo Jet Skis',		'86', '128389', '176839'),
	('BT_1014', 'Slow Jet Skis',		'73', '375764', '430202'),
	('BT_1015', 'Never A Dull Moment',	'74', '188237', '262844'),
	('BT_1016', 'Sleep The Day Away',	'76', '130525', '177625'),
	('BT_1017', 'Always Awake',		'76', '201826', '266086'),
	('BT_1018', 'Forget Me Not',		'75', '110313', '169152');

SELECT *
FROM Products_Table
