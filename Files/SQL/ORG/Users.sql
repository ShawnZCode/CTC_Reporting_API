/****** Object:  Table [dbo].[Users]    Script Date: 11/17/2022 4:29:01 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[Users](
	[id] [uniqueidentifier] NOT NULL,
	[displayName] [nvarchar](100) NOT NULL,
	[updatedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_Users] PRIMARY KEY CLUSTERED 
	(
		[id] ASC
	)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]

