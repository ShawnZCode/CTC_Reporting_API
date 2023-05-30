/****** Object:  Table [CMS].[SavedSearchTags]    Script Date: 11/17/2022 4:25:31 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [CMS].[SavedSearchTags](
	[savedSearchId] [uniqueidentifier] NOT NULL,
	[tagId] [uniqueidentifier] NOT NULL,
	[refreshedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_SavedSearchTags] PRIMARY KEY CLUSTERED 
	(
		[savedSearchId] ASC,
		[tagId] ASC
	)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]