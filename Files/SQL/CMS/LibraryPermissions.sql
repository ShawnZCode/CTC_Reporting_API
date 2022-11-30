/****** Object:  Table [dbo].[LibraryPermissions]    Script Date: 11/17/2022 4:22:54 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[LibraryPermissions](
	[id] [uniqueidentifier] NOT NULL,
	[addedAt] [datetime2](7) NOT NULL,
	[addedById] [uniqueidentifier] NOT NULL,
	[updatedAt] [datetime2](7) NOT NULL,
	[updatedById] [uniqueidentifier] NOT NULL,
	[libraryId] [uniqueidentifier] NOT NULL,
	[resourceId] [uniqueidentifier] NOT NULL,
	[resourceType] [int] NOT NULL,
	[role] [int] NOT NULL,
	[librarySubscriptionId] [uniqueidentifier] NULL,
	[resourceSource] [int] NOT NULL,
	[refreshedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_LibraryPermissions] PRIMARY KEY CLUSTERED 
		([id] ASC)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]

ALTER TABLE [dbo].[LibraryPermissions] ADD  DEFAULT ((0)) FOR [resourceSource]
