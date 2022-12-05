/****** Object:  Table [dbo].[SavedSearchLibraries]    Script Date: 11/17/2022 4:24:17 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[SavedSearchLibraries](
	[savedSearchId] [uniqueidentifier] NOT NULL,
	[libraryId] [uniqueidentifier] NOT NULL,
	[refreshedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_SavedSearchLibraries] PRIMARY KEY CLUSTERED 
	(
		[savedSearchId] ASC,
		[libraryId] ASC
	)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
