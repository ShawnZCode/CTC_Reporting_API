/****** Object:  Table [dbo].[SearchLibraries]    Script Date: 11/17/2022 4:27:02 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[SearchLibraries](
	[searchId] [uniqueidentifier] NOT NULL,
	[libraryId] [uniqueidentifier] NOT NULL,
	[libraryName] [nvarchar](100) NOT NULL,
	[refreshedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_SearchLibraries] PRIMARY KEY CLUSTERED 
	(
		[searchId] ASC,
		[libraryId] ASC
	)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
