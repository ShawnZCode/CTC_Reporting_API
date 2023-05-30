/****** Object:  Table [CMS].[SavedSearchCategories]    Script Date: 11/17/2022 4:25:10 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [CMS].[SavedSearchCategories](
	[savedSearchId] [uniqueidentifier] NOT NULL,
	[categoryId] [int] NOT NULL,
	[refreshedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_SavedSearchCategories] PRIMARY KEY CLUSTERED 
	(
		[savedSearchId] ASC,
		[categoryId] ASC
	)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
