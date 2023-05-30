/****** Object:  Table [CMS].[SavedSearchPermissions]    Script Date: 11/17/2022 4:24:40 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [CMS].[SavedSearchPermissions](
	[id] [uniqueidentifier] NOT NULL,
	[addedAt] [datetime2](7) NOT NULL,
	[addedById] [uniqueidentifier] NOT NULL,
	[updatedAt] [datetime2](7) NOT NULL,
	[updatedById] [uniqueidentifier] NOT NULL,
	[savedSearchId] [uniqueidentifier] NOT NULL,
	[resourceId] [uniqueidentifier] NOT NULL,
	[resourceType] [int] NOT NULL,
	[refreshedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_SavedSearchPermissions] PRIMARY KEY CLUSTERED 
	(
		[id] ASC
	)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]

ALTER TABLE [CMS].[SavedSearchPermissions] ADD  DEFAULT ('00000000-0000-0000-0000-000000000000') FOR [resourceId]

ALTER TABLE [CMS].[SavedSearchPermissions] ADD  DEFAULT ((0)) FOR [resourceType]
