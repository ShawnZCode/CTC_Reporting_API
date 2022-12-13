/****** Object:  Table [CMS].[SearchContentSources]    Script Date: 11/17/2022 4:26:20 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [CMS].[SearchContentSources](
	[searchId] [uniqueidentifier] NOT NULL,
	[contentSource] [int] NOT NULL,
	[refreshedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_SearchContentSources] PRIMARY KEY CLUSTERED 
	(
		[searchId] ASC,
		[contentSource] ASC
	)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
