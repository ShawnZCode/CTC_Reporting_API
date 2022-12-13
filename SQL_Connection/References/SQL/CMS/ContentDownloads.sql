/****** Object:  Table [CMS].[ContentDownloads]    Script Date: 11/17/2022 4:21:13 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [CMS].[ContentDownloads](
	[id] [uniqueidentifier] NOT NULL,
	[contentId] [uniqueidentifier] NOT NULL,
	[downloadedAt] [datetime2](7) NOT NULL,
	[downloadedById] [uniqueidentifier] NOT NULL,
	[refreshedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_ContentDownloads] PRIMARY KEY CLUSTERED 
		([id] ASC)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]

ALTER TABLE [CMS].[ContentDownloads] ADD  DEFAULT ('0001-01-01T00:00:00.0000000') FOR [downloadedAt]

ALTER TABLE [CMS].[ContentDownloads] ADD  DEFAULT ('00000000-0000-0000-0000-000000000000') FOR [downloadedById]
