/****** Object:  Table [dbo].[ContentTags]    Script Date: 11/17/2022 4:21:46 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[ContentTags](
	[tagId] [uniqueidentifier] NOT NULL,
	[contentId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_ContentTags] PRIMARY KEY CLUSTERED 
	(
		[tagId] ASC,
		[contentId] ASC
	)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
