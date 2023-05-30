/****** Object:  Table [CMS].[ContentRevisions]    Script Date: 11/17/2022 4:18:43 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON


CREATE TABLE [CMS].[ContentRevisions](
	[id] [uniqueidentifier] NOT NULL,
	[contentId] [uniqueidentifier] NOT NULL,
	[comment] [nvarchar](2048) NULL,
	[revisedAt] [datetime2](7) NOT NULL,
	[revisedById] [uniqueidentifier] NOT NULL,
	[refreshedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_ContentRevisions] PRIMARY KEY CLUSTERED 
	(
		[id] ASC
	)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]

ALTER TABLE [CMS].[ContentRevisions] ADD  DEFAULT ('0001-01-01T00:00:00.0000000') FOR [revisedAt]

ALTER TABLE [CMS].[ContentRevisions] ADD  DEFAULT ('00000000-0000-0000-0000-000000000000') FOR [revisedById]
