/****** Object:  Table [dbo].[SearchRevitCategories]    Script Date: 11/17/2022 4:27:45 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[SearchRevitCategories](
	[searchId] [uniqueidentifier] NOT NULL,
	[revitCategoryId] [int] NOT NULL,
	[updatedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_SearchRevitCategories] PRIMARY KEY CLUSTERED 
	(
		[searchId] ASC,
		[revitCategoryId] ASC
	)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
