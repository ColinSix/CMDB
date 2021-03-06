CREATE TABLE user (
  id int(11) NOT NULL AUTO_INCREMENT,
  username varchar(25) NOT NULL,
  password varchar(32) NOT NULL,
  role varchar(25) NOT NULL,
  email varchar(50) DEFAULT NULL,
  cname varchar(25) DEFAULT NULL,
  url varchar(50) DEFAULT NULL,
  token varchar(32) DEFAULT NULL,
  extra varchar(500) DEFAULT NULL,
  PRIMARY KEY (id,username));


CREATE TABLE vmassets (
  id int(11) NOT NULL AUTO_INCREMENT,
  room varchar(25) DEFAULT NULL,
  pool varchar(255) DEFAULT NULL,
  project varchar(255) DEFAULT NULL,
  vmname varchar(255) DEFAULT NULL,
  ip varchar(25) NOT NULL,
  cpu varchar(25) DEFAULT NULL,
  memory varchar(25) DEFAULT NULL,
  disk varchar(25) DEFAULT NULL,
  system varchar(255) DEFAULT NULL,
  hostname varchar(255) DEFAULT NULL,
  user varchar(255) DEFAULT NULL,
  password varchar(255) DEFAULT NULL,
  contact varchar(255) DEFAULT NULL,
  cphone varchar(255) DEFAULT NULL,
  bank varchar(255) DEFAULT NULL,
  bphone varchar(255) DEFAULT NULL,
  startdate varchar(255) DEFAULT NULL,
  enddate varchar(255) DEFAULT NULL,
  note varchar(255) DEFAULT NULL,
  PRIMARY KEY (id,ip));

insert into user (username, password, role, email) values ("John", "123456", "admin", "123@cdb.com");
insert into user (username, password, role, email) values ("Aaron", "123456", "admin", "123@cdb.com");
insert into user (username, password, role, email) values ("Lisa", "123456", "admin", "123@cdb.com");

insert into vmassets (ip_addr,app_name,hostname,vc_name,cpu,memory,disk,os,status,office_name,office_contact,office_phone,object_contact,object_phone,create_date,end_date,notes) values ("10.66.207.138","开发测试yum源","ftp.cdb.com","BEJOVE0516","8C","16G","500G","Redhat6.6 64bit","正在使用","开发测试综合处","明广振","88303114","明广振","88303114","2015-08-20","2020-12-12","开发测试服务器")


sql = 'update user set password="%s",role="%s",email="%s" where id="%s"' % (password,role,email,userid)

sqlkeys = str(['username', 'password', 'role', 'email']).replace("[","").replace("]","").replace("'","").replace(",","='%s',") + "='%s'"

['username', 'password', 'role', 'email']
','.join(['username', 'password', 'role', 'email'])


CREATE USER 'username'@'host' IDENTIFIED BY 'password'; 
CREATE USER 'mingguangzhen'@'%' IDENTIFIED BY '123456';


GRANT privileges ON databasename.tablename TO 'username'@'host' 

GRANT SELECT, INSERT ON test.user TO 'pig'@'%'; 
GRANT privileges ON databasename.tablename TO 'username'@'host' WITH GRANT OPTION; 
GRANT ALL ON *.* TO 'mingguangzhen'@'%' WITH GRANT OPTION; 


flush privileges;