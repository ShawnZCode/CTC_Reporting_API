/****** Object:  Table [dbo].[ContentLibraries]    Script Date: 11/17/2022 4:19:36 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[ContentLibraries](
	[libraryId] [uniqueidentifier] NOT NULL,
	[contentId] [uniqueidentifier] NOT NULL,
	[refreshedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_ContentLibraries] PRIMARY KEY CLUSTERED 
	(
		[contentId] ASC,
		[libraryId] ASC
	)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
