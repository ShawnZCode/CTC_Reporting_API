/****** Object:  Table [dbo].[ContentAttachments]    Script Date: 11/17/2022 4:21:31 PM ******/
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[ContentAttachments](
	[id] [uniqueidentifier] NOT NULL,
	[addedAt] [datetime2](7) NOT NULL,
	[addedById] [uniqueidentifier] NOT NULL,
	[updatedAt] [datetime2](7) NOT NULL,
	[updatedById] [uniqueidentifier] NOT NULL,
	[fileExtension] [nvarchar](10) NULL,
	[fileSizeInBytes] [bigint] NULL,
	[organizationId] [uniqueidentifier] NOT NULL,
	[contentId] [uniqueidentifier] NOT NULL,
	[description] [nvarchar](2048) NULL,
	[isLink] [bit] NOT NULL,
	[name] [nvarchar](2048) NOT NULL,
	[path] [nvarchar](2048) NOT NULL,
	[type] [int] NOT NULL,
	CONSTRAINT [PK_ContentAttachments] PRIMARY KEY CLUSTERED 
		([Id] ASC)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
ALTER TABLE [dbo].[ContentAttachments] ADD  DEFAULT (CONVERT([bit],(0))) FOR [IsLink]
ALTER TABLE [dbo].[ContentAttachments] ADD  DEFAULT (N'') FOR [Name]
ALTER TABLE [dbo].[ContentAttachments] ADD  DEFAULT (N'') FOR [Path]
ALTER TABLE [dbo].[ContentAttachments] ADD  DEFAULT ((100)) FOR [Type]
