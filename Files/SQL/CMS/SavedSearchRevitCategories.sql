/****** Object:  Table [dbo].[SavedSearchRevitCategories]    Script Date: 11/17/2022 4:25:10 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[SavedSearchRevitCategories](
	[savedSearchId] [uniqueidentifier] NOT NULL,
	[revitCategoryId] [int] NOT NULL,
	CONSTRAINT [PK_SavedSearchRevitCategories] PRIMARY KEY CLUSTERED 
	(
		[savedSearchId] ASC,
		[revitCategoryId] ASC
	)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
