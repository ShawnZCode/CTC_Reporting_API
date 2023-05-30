/****** Object:  Table [Accounts].[Users]    Script Date: 11/17/2022 4:29:01 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [Accounts].[Users](
	[id] [uniqueidentifier] NOT NULL,
	[firstName] [nvarchar](100) NOT NULL,
	[lastName] [nvarchar](100) NOT NULL,
	[displayName] [nvarchar](100) NOT NULL,
	[description] [nvarchar](250) NOT NULL,
	[office] [nvarchar](100) NOT NULL,
	[department] [nvarchar](100) NOT NULL,
	[lastLoggedInAt] [datetime2](7) NOT NULL,
	[status] [nvarchar](20) NOT NULL,
	[adDomainSystemId] [uniqueidentifier] NULL,
	[adSamAccountName] [nvarchar](100) NULL,
	[createdAt] [datetime2](7) NOT NULL,
	[createdById] [uniqueidentifier] NOT NULL,
	[updatedAt] [datetime2](7) NOT NULL,
	[updatedById] [uniqueidentifier] NOT NULL,
	[isSSOUser] [bit] NOT NULL,
	[refreshedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_Users] PRIMARY KEY CLUSTERED 
	(
		[id] ASC
	)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
