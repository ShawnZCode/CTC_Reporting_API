/****** Object:  Table [Accounts].[Groups]    Script Date: 11/17/2022 4:29:01 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [Accounts].[Groups](
	[id] [uniqueidentifier] NOT NULL,
	[name] [nvarchar](100) NOT NULL,
	[description] [nvarchar](250) NOT NULL,
	[adSystemId] [uniqueidentifier] NULL,
	[adDomainSystemId] [uniqueidentifier] NULL,
	[adSamAccountName] [nvarchar](100) NULL,
	[createdAt] [datetime2](7) NOT NULL,
	[createdById] [uniqueidentifier] NOT NULL,
	[updatedAt] [datetime2](7) NOT NULL,
	[updatedById] [uniqueidentifier] NOT NULL,
	[isDefaultGroup] [bit] NOT NULL,
	[refreshedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_Groups] PRIMARY KEY CLUSTERED 
	(
		[id] ASC
	)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
