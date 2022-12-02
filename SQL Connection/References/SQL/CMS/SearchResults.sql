/****** Object:  Table [dbo].[SearchResults]    Script Date: 11/17/2022 4:27:19 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[SearchResults](
	[searchId] [uniqueidentifier] NOT NULL,
	[contentId] [uniqueidentifier] NOT NULL,
	[contentName] [nvarchar](150) NOT NULL,
	[refreshedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_SearchResults] PRIMARY KEY CLUSTERED 
	(
		[searchId] ASC,
		[contentId] ASC
	)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
