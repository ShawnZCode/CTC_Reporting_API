/****** Object:  Table [dbo].[SearchTags]    Script Date: 11/17/2022 4:28:01 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[SearchTags](
	[searchId] [uniqueidentifier] NOT NULL,
	[tagId] [uniqueidentifier] NOT NULL,
	[tagName] [nvarchar](100) NOT NULL,
	CONSTRAINT [PK_SearchTags] PRIMARY KEY CLUSTERED 
	(
		[searchId] ASC,
		[tagId] ASC
	)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
