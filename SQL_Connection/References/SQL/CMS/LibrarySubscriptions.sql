/****** Object:  Table [CMS].[LibrarySubscriptions]    Script Date: 11/30/2022 1:29:00 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [CMS].[LibrarySubscriptions](
	[Id] [uniqueidentifier] NOT NULL,
	[OrganizationId] [uniqueidentifier] NOT NULL,
	[LibraryId] [uniqueidentifier] NOT NULL,
	[SubscribedAt] [datetime2](7) NOT NULL,
	[SubscribedById] [uniqueidentifier] NOT NULL,
	[ExpirationDate] [datetime2](7) NULL,
    [refreshedId] [uniqueidentifier] NOT NULL,
 CONSTRAINT [PK_LibrarySubscriptions] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]

ALTER TABLE [CMS].[LibrarySubscriptions] ADD  DEFAULT ('0001-01-01T00:00:00.0000000') FOR [SubscribedAt]

ALTER TABLE [CMS].[LibrarySubscriptions] ADD  DEFAULT ('00000000-0000-0000-0000-000000000000') FOR [SubscribedById]
