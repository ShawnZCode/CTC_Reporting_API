/****** Object:  Table [dbo].[ContentLoads]    Script Date: 11/17/2022 4:19:20 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[ContentLoads](
	[id] [uniqueidentifier] NOT NULL,
	[contentId] [uniqueidentifier] NOT NULL,
	[loadedAt] [datetime2](7) NOT NULL,
	[loadedById] [uniqueidentifier] NOT NULL,
	[documentId] [uniqueidentifier] NULL,
	[searchId] [uniqueidentifier] NULL,
	[refreshedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_ContentLoads] PRIMARY KEY CLUSTERED 
		([id] ASC)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]

ALTER TABLE [dbo].[ContentLoads] ADD  DEFAULT ('00000000-0000-0000-0000-000000000000') FOR [loadedById]
