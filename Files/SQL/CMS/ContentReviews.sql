/****** Object:  Table [dbo].[ContentReviews]    Script Date: 11/17/2022 4:19:03 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[ContentReviews](
	[id] [uniqueidentifier] NOT NULL,
	[addedAt] [datetime2](7) NOT NULL,
	[addedById] [uniqueidentifier] NOT NULL,
	[updatedAt] [datetime2](7) NOT NULL,
	[updatedById] [uniqueidentifier] NOT NULL,
	[contentId] [uniqueidentifier] NOT NULL,
	[rating] [int] NOT NULL,
	[comment] [nvarchar](2048) NULL,
	[updatedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_ContentReviews] PRIMARY KEY CLUSTERED 
		([id] ASC) WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
