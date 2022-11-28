/****** Object:  Table [dbo].[ContentFiles]    Script Date: 11/17/2022 4:19:56 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[ContentFiles](
	[id] [uniqueidentifier] NOT NULL,
	[addedAt] [datetime2](7) NOT NULL,
	[addedById] [uniqueidentifier] NOT NULL,
	[updatedAt] [datetime2](7) NOT NULL,
	[updatedById] [uniqueidentifier] NOT NULL,
	[fileName] [nvarchar](150) NOT NULL,
	[filePath] [nvarchar](255) NOT NULL,
	[fileExtension] [nvarchar](13) NOT NULL,
	[fileSizeInBytes] [bigint] NOT NULL,
	[fileCreatedAt] [datetime2](7) NOT NULL,
	[fileModifiedAt] [datetime2](7) NOT NULL,
	[fileVersion] [int] NOT NULL,
	[contentId] [uniqueidentifier] NOT NULL,
	[organizationId] [uniqueidentifier] NOT NULL,
	[hasRevitTypeCatalog] [bit] NULL,
	[revitSourceProjectElementId] [int] NULL,
	[revitContainerProjectElementId] [int] NULL,
	[revitCentralProjectFilePath] [nvarchar](255) NULL,
	[revitProjectWorkSharingMode] [int] NULL,
	[location] [nvarchar](25) NOT NULL,
	[updatedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_ContentFiles] PRIMARY KEY CLUSTERED 
		([id] ASC)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]

ALTER TABLE [dbo].[ContentFiles] ADD  DEFAULT ('cloud') FOR [location]
