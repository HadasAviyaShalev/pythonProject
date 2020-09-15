create database pythonProject
go
use pythonProject
go
create table Customer
(
	CustomerCode int primary key identity (1,1),
	CustomerId varchar(9),
	FirstName varchar(20),
	LastName varchar(20),
	CustomerAddress varchar(50),
	Country varchar(20)
)
create table CallRoue
(
	CodeRoute int primary key identity (1,1),
	NameRoue varchar(20),
	CostRoue int,
	MinutesHere int,
	MinuteAbroad int

)
create table Line
(
	LineCode int identity (1,1),
	CustomerCode int foreign key references Customer(CustomerCode),
	RouteCode int foreign key references CallRoue(CodeRoute),
	Phone varchar(10),
	constraint line primary key(Phone),
	constraint line unique(Phone)
)
create table Talking
(
	TalkCode int primary key identity (1,1),
	StartDate date,
	EndDate date,
	FromPhone varchar(10) foreign key references Line(Phone),
	ToPhone varchar(10) foreign key references Line(Phone)
)

