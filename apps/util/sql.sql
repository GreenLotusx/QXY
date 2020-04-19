DROP DATABASE IF EXISTS db_qxy;

create database if not exists db_qxy default character set utf8 collate utf8_general_ci;

use db_qxy;

create table if not exists tab_file(
	f_id bigint auto_increment comment '文件id',
	f_type varchar(32) comment '文件类型',
	f_inittime datetime not null default current_timestamp  comment '源上传时间',
	f_inituse int not null comment '源用户',
	f_size int not null default 1 comment '文件大小',
	f_count int not null comment '引用次数',
	f_md5 varchar(64) not null comment '文件md5',
	f_path varchar(128) not null comment '文件所在路径',		
	PRIMARY KEY (f_id),
	unique(f_id)
) engine=InnoDB default charset=utf8 comment '文件表';

DROP TABLE IF EXISTS tab_user_infos;

create table if not exists tab_user(
	u_id bigint auto_increment comment '用户id',			
	u_name varchar(12) not null comment '用户名',					
	u_salt varchar(128) not null comment '密码密文',
	u_nickname varchar(32) not null comment '用户昵称',
	u_email varchar(64) not null comment "用户邮箱",
	u_time bigint not null comment '用户创建时间',
	u_data text comment '用户文件信息数据',
	u_size bigint not null comment '可用大小',
	u_totalsize bigint not null comment '总大小',
	ui_identity int default 2 comment '用户权限',			
	PRIMARY KEY (u_id),
	unique(u_id)
) engine=InnoDB default charset=utf8 comment '用户表';

create table if not exists tab_identity(
	i_id int auto_increment comment '权限id',			
	i_lv int not null comment '权限级别',					
	i_limitup int not null default 0 comment '限制上传速度',
	i_limitdown int not null default 0 comment '限制下载速度',
	i_view text comment '支持预览文件类型',				
	PRIMARY KEY (i_id),
	unique(i_id)
) engine=InnoDB default charset=utf8 comment '权限表';
