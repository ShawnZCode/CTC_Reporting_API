/****** Object:  Table [dbo].[Libraries]    Script Date: 11/17/2022 4:22:34 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[Libraries](
	[id] [uniqueidentifier] NOT NULL,
	[addedAt] [datetime2](7) NOT NULL,
	[addedById] [uniqueidentifier] NOT NULL,
	[updatedAt] [datetime2](7) NOT NULL,
	[updatedById] [uniqueidentifier] NOT NULL,
	[name] [nvarchar](100) NOT NULL,
	[organizationId] [uniqueidentifier] NOT NULL,
	[type] [nvarchar](15) NOT NULL,
	[description] [nvarchar](2048) NULL,
	[uploadContent] [bit] NOT NULL,
	[defaultRole] [nvarchar](15) NOT NULL,
	[imageUri] [nvarchar](2048) NULL,
	[updatedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_Libraries] PRIMARY KEY CLUSTERED 
		([id] ASC)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]

ALTER TABLE [dbo].[Libraries] ADD  DEFAULT ((200)) FOR [defaultRole]
