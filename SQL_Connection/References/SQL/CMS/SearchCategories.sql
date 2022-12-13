/****** Object:  Table [CMS].[SearchCategories]    Script Date: 11/17/2022 4:27:45 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [CMS].[SearchCategories](
	[searchId] [uniqueidentifier] NOT NULL,
	[categoryId] [int] NOT NULL,
	[refreshedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_SearchCategories] PRIMARY KEY CLUSTERED 
	(
		[searchId] ASC,
		[categoryId] ASC
	)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
