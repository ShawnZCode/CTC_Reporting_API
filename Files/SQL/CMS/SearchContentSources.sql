/****** Object:  Table [dbo].[SearchContentSources]    Script Date: 11/17/2022 4:26:20 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[SearchContentSources](
	[searchId] [uniqueidentifier] NOT NULL,
	[contentSource] [int] NOT NULL,
	[updatedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_SearchContentSources] PRIMARY KEY CLUSTERED 
	(
		[searchId] ASC,
		[contentSource] ASC
	)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
