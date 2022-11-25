/****** Object:  Table [dbo].[UserFavoriteContents]    Script Date: 11/17/2022 4:28:45 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[UserFavoriteContents](
	[userId] [uniqueidentifier] NOT NULL,
	[contentId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_UserFavoriteContents] PRIMARY KEY CLUSTERED 
	(
		[userId] ASC,
		[contentId] ASC
	)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
