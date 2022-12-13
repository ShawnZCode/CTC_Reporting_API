/****** Object:  Table [CMS].[SavedSearchContentSources]    Script Date: 11/17/2022 4:23:27 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [CMS].[SavedSearchContentSources](
	[savedSearchId] [uniqueidentifier] NOT NULL,
	[contentSource] [int] NOT NULL,
	[refreshedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_SavedSearchContentSources] PRIMARY KEY CLUSTERED 
	(
		[savedSearchId] ASC,
		[contentSource] ASC
	)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
