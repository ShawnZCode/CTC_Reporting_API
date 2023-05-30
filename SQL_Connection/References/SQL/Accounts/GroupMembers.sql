/****** Object:  Table [Accounts].[GroupMembers]    Script Date: 11/17/2022 4:29:01 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [Accounts].[GroupMembers](
	[groupId] [uniqueidentifier] NOT NULL,
	[userId] [uniqueidentifier] NOT NULL,
	[refreshedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_GroupMembers] PRIMARY KEY CLUSTERED 
	(
		[groupid] ASC,
		[userId] ASC
	)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
