
/*** Alter Categories ***/
ALTER TABLE [CMS].[Categories]  WITH CHECK ADD  CONSTRAINT [FK_Categories_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[Categories] CHECK CONSTRAINT [FK_Categories_Refreshed_refreshedId]

/*** Alter Contents ***/
ALTER TABLE [CMS].[Contents]  WITH CHECK ADD  CONSTRAINT [FK_Contents_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [Accounts].[Users] ([id])

ALTER TABLE [CMS].[Contents] CHECK CONSTRAINT [FK_Contents_Users_addedById]

ALTER TABLE [CMS].[Contents]  WITH CHECK ADD  CONSTRAINT [FK_Contents_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [Accounts].[Users] ([id])

ALTER TABLE [CMS].[Contents] CHECK CONSTRAINT [FK_Contents_Users_updatedById]

ALTER TABLE [CMS].[Contents]  WITH CHECK ADD  CONSTRAINT [FK_Contents_Categories_categoryId] FOREIGN KEY([categoryId])
REFERENCES [CMS].[Categories] ([id])

ALTER TABLE [CMS].[Contents] CHECK CONSTRAINT [FK_Contents_Categories_categoryId]

ALTER TABLE [CMS].[Contents]  WITH CHECK ADD  CONSTRAINT [FK_Contents_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[Contents] CHECK CONSTRAINT [FK_Contents_Refreshed_refreshedId]

/*** Alter ContentAtachments ***/
ALTER TABLE [CMS].[ContentAttachments]  WITH CHECK ADD  CONSTRAINT [FK_ContentAttachments_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [CMS].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[ContentAttachments] CHECK CONSTRAINT [FK_ContentAttachments_Contents_contentId]

ALTER TABLE [CMS].[ContentAttachments]  WITH CHECK ADD  CONSTRAINT [FK_ContentAttachments_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [Accounts].[Users] ([id])

ALTER TABLE [CMS].[ContentAttachments] CHECK CONSTRAINT [FK_ContentAttachments_Users_addedById]

ALTER TABLE [CMS].[ContentAttachments]  WITH CHECK ADD  CONSTRAINT [FK_ContentAttachments_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [Accounts].[Users] ([id])

ALTER TABLE [CMS].[ContentAttachments] CHECK CONSTRAINT [FK_ContentAttachments_Users_updatedById]

ALTER TABLE [CMS].[ContentAttachments]  WITH CHECK ADD  CONSTRAINT [FK_ContentAttachments_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[ContentAttachments] CHECK CONSTRAINT [FK_ContentAttachments_Refreshed_refreshedId]

/*** Alter ContentDownloads ***/
ALTER TABLE [CMS].[ContentDownloads]  WITH CHECK ADD  CONSTRAINT [FK_ContentDownloads_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [CMS].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[ContentDownloads] CHECK CONSTRAINT [FK_ContentDownloads_Contents_contentId]

ALTER TABLE [CMS].[ContentDownloads]  WITH CHECK ADD  CONSTRAINT [FK_ContentDownloads_Users_downloadedById] FOREIGN KEY([downloadedById])
REFERENCES [Accounts].[Users] ([id])

ALTER TABLE [CMS].[ContentDownloads] CHECK CONSTRAINT [FK_ContentDownloads_Users_downloadedById]

ALTER TABLE [CMS].[ContentDownloads]  WITH CHECK ADD  CONSTRAINT [FK_ContentDownloads_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[ContentDownloads] CHECK CONSTRAINT [FK_ContentDownloads_Refreshed_refreshedId]

/*** Alter ContentFileComponentProperties ***/
ALTER TABLE [CMS].[ContentFileComponentProperties]  WITH CHECK ADD  CONSTRAINT [FK_ContentFileComponentProperties_ContentFileComponents_contentFileComponentId] FOREIGN KEY([contentFileComponentId])
REFERENCES [CMS].[ContentFileComponents] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[ContentFileComponentProperties] CHECK CONSTRAINT [FK_ContentFileComponentProperties_ContentFileComponents_contentFileComponentId]

ALTER TABLE [CMS].[ContentFileComponentProperties]  WITH CHECK ADD  CONSTRAINT [FK_ContentFileComponentProperties_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[ContentFileComponentProperties] CHECK CONSTRAINT [FK_ContentFileComponentProperties_Refreshed_refreshedId]

/*** Alter ContentFileComponents ***/
ALTER TABLE [CMS].[ContentFileComponents]  WITH CHECK ADD  CONSTRAINT [FK_ContentFileComponents_ContentFiles_contentFileId] FOREIGN KEY([contentFileId])
REFERENCES [CMS].[ContentFiles] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[ContentFileComponents] CHECK CONSTRAINT [FK_ContentFileComponents_ContentFiles_contentFileId]

ALTER TABLE [CMS].[ContentFileComponents]  WITH CHECK ADD  CONSTRAINT [FK_ContentFileComponents_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[ContentFileComponents] CHECK CONSTRAINT [FK_ContentFileComponents_Refreshed_refreshedId]

/*** Alter ContentFiles ***/
ALTER TABLE [CMS].[ContentFiles]  WITH CHECK ADD  CONSTRAINT [FK_ContentFiles_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [CMS].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[ContentFiles] CHECK CONSTRAINT [FK_ContentFiles_Contents_contentId]

ALTER TABLE [CMS].[ContentFiles]  WITH CHECK ADD  CONSTRAINT [FK_ContentFiles_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [Accounts].[Users] ([id])

ALTER TABLE [CMS].[ContentFiles] CHECK CONSTRAINT [FK_ContentFiles_Users_addedById]

ALTER TABLE [CMS].[ContentFiles]  WITH CHECK ADD  CONSTRAINT [FK_ContentFiles_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [Accounts].[Users] ([id])

ALTER TABLE [CMS].[ContentFiles] CHECK CONSTRAINT [FK_ContentFiles_Users_updatedById]

ALTER TABLE [CMS].[ContentFiles]  WITH CHECK ADD  CONSTRAINT [FK_ContentFiles_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[ContentFiles] CHECK CONSTRAINT [FK_ContentFiles_Refreshed_refreshedId]

/*** Alter ContentLibraries ***/
ALTER TABLE [CMS].[ContentLibraries]  WITH CHECK ADD  CONSTRAINT [FK_ContentLibraries_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [CMS].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[ContentLibraries] CHECK CONSTRAINT [FK_ContentLibraries_Contents_contentId]

ALTER TABLE [CMS].[ContentLibraries]  WITH CHECK ADD  CONSTRAINT [FK_ContentLibraries_Libraries_libraryId] FOREIGN KEY([libraryId])
REFERENCES [CMS].[Libraries] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[ContentLibraries] CHECK CONSTRAINT [FK_ContentLibraries_Libraries_libraryId]

ALTER TABLE [CMS].[ContentLibraries]  WITH CHECK ADD  CONSTRAINT [FK_ContentLibraries_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[ContentLibraries] CHECK CONSTRAINT [FK_ContentLibraries_Refreshed_refreshedId]

/*** Alter ContentLoads ***/

ALTER TABLE [CMS].[ContentLoads]  WITH CHECK ADD  CONSTRAINT [FK_ContentLoads_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [CMS].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[ContentLoads] CHECK CONSTRAINT [FK_ContentLoads_Contents_contentId]

ALTER TABLE [CMS].[ContentLoads]  WITH CHECK ADD  CONSTRAINT [FK_ContentLoads_Documents_documentId] FOREIGN KEY([documentId])
REFERENCES [CMS].[Documents] ([id])

ALTER TABLE [CMS].[ContentLoads] CHECK CONSTRAINT [FK_ContentLoads_Documents_documentId]

ALTER TABLE [CMS].[ContentLoads]  WITH CHECK ADD  CONSTRAINT [FK_ContentLoads_Searches_searchId] FOREIGN KEY([searchId])
REFERENCES [CMS].[Searches] ([id])

ALTER TABLE [CMS].[ContentLoads] CHECK CONSTRAINT [FK_ContentLoads_Searches_searchId]

ALTER TABLE [CMS].[ContentLoads]  WITH CHECK ADD  CONSTRAINT [FK_ContentLoads_Users_loadedById] FOREIGN KEY([loadedById])
REFERENCES [Accounts].[Users] ([id])

ALTER TABLE [CMS].[ContentLoads] CHECK CONSTRAINT [FK_ContentLoads_Users_loadedById]

ALTER TABLE [CMS].[ContentLoads]  WITH CHECK ADD  CONSTRAINT [FK_ContentLoads_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[ContentLoads] CHECK CONSTRAINT [FK_ContentLoads_Refreshed_refreshedId]

/*** Alter ContentReviews ***/
ALTER TABLE [CMS].[ContentReviews]  WITH CHECK ADD  CONSTRAINT [FK_ContentReviews_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [CMS].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[ContentReviews] CHECK CONSTRAINT [FK_ContentReviews_Contents_contentId]

ALTER TABLE [CMS].[ContentReviews]  WITH CHECK ADD  CONSTRAINT [FK_ContentReviews_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [Accounts].[Users] ([id])

ALTER TABLE [CMS].[ContentReviews] CHECK CONSTRAINT [FK_ContentReviews_Users_addedById]

ALTER TABLE [CMS].[ContentReviews]  WITH CHECK ADD  CONSTRAINT [FK_ContentReviews_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [Accounts].[Users] ([id])

ALTER TABLE [CMS].[ContentReviews] CHECK CONSTRAINT [FK_ContentReviews_Users_updatedById]

ALTER TABLE [CMS].[ContentReviews]  WITH CHECK ADD  CONSTRAINT [FK_ContentReviews_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[ContentReviews] CHECK CONSTRAINT [FK_ContentReviews_Refreshed_refreshedId]

/*** Content Revisions ***/
ALTER TABLE [CMS].[ContentRevisions]  WITH CHECK ADD  CONSTRAINT [FK_ContentRevisions_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [CMS].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[ContentRevisions] CHECK CONSTRAINT [FK_ContentRevisions_Contents_contentId]

ALTER TABLE [CMS].[ContentRevisions]  WITH CHECK ADD  CONSTRAINT [FK_ContentRevisions_Users_revisedById] FOREIGN KEY([revisedById])
REFERENCES [Accounts].[Users] ([id])

ALTER TABLE [CMS].[ContentRevisions] CHECK CONSTRAINT [FK_ContentRevisions_Users_revisedById]

ALTER TABLE [CMS].[ContentRevisions]  WITH CHECK ADD  CONSTRAINT [FK_ContentRevisions_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[ContentRevisions] CHECK CONSTRAINT [FK_ContentRevisions_Refreshed_refreshedId]

/*** Alter ContentTags ***/
ALTER TABLE [CMS].[ContentTags]  WITH CHECK ADD  CONSTRAINT [FK_ContentTags_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [CMS].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[ContentTags] CHECK CONSTRAINT [FK_ContentTags_Contents_contentId]

ALTER TABLE [CMS].[ContentTags]  WITH CHECK ADD  CONSTRAINT [FK_ContentTags_Tags_tagId] FOREIGN KEY([tagId])
REFERENCES [CMS].[Tags] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[ContentTags] CHECK CONSTRAINT [FK_ContentTags_Tags_tagId]

ALTER TABLE [CMS].[ContentTags]  WITH CHECK ADD  CONSTRAINT [FK_ContentTags_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[ContentTags] CHECK CONSTRAINT [FK_ContentTags_Refreshed_refreshedId]

/*** Alter Documents (NotNeeded) ***/
ALTER TABLE [CMS].[Documents]  WITH CHECK ADD  CONSTRAINT [FK_Documents_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[Documents] CHECK CONSTRAINT [FK_Documents_Refreshed_refreshedId]

/*** Alter Feedbacks ***/
ALTER TABLE [CMS].[Feedbacks]  WITH CHECK ADD  CONSTRAINT [FK_Feedbacks_Users_submittedById] FOREIGN KEY([submittedById])
REFERENCES [Accounts].[Users] ([id])

ALTER TABLE [CMS].[Feedbacks] CHECK CONSTRAINT [FK_Feedbacks_Users_submittedById]

ALTER TABLE [CMS].[Feedbacks]  WITH CHECK ADD  CONSTRAINT [FK_Feedbacks_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[Feedbacks] CHECK CONSTRAINT [FK_Feedbacks_Refreshed_refreshedId]

/*** Alter Libraries ***/
ALTER TABLE [CMS].[Libraries]  WITH CHECK ADD  CONSTRAINT [FK_Libraries_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [Accounts].[Users] ([id])

ALTER TABLE [CMS].[Libraries] CHECK CONSTRAINT [FK_Libraries_Users_addedById]

ALTER TABLE [CMS].[Libraries]  WITH CHECK ADD  CONSTRAINT [FK_Libraries_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [Accounts].[Users] ([id])

ALTER TABLE [CMS].[Libraries] CHECK CONSTRAINT [FK_Libraries_Users_updatedById]

ALTER TABLE [CMS].[Libraries]  WITH CHECK ADD  CONSTRAINT [FK_Libraries_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[Libraries] CHECK CONSTRAINT [FK_Libraries_Refreshed_refreshedId]

/*** Alter LibraryPermissions ***/
ALTER TABLE [CMS].[LibraryPermissions]  WITH CHECK ADD  CONSTRAINT [FK_LibraryPermissions_Libraries_libraryId] FOREIGN KEY([libraryId])
REFERENCES [CMS].[Libraries] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[LibraryPermissions] CHECK CONSTRAINT [FK_LibraryPermissions_Libraries_libraryId]

ALTER TABLE [CMS].[LibraryPermissions]  WITH CHECK ADD  CONSTRAINT [FK_LibraryPermissions_LibrarySubscriptions_librarySubscriptionId] FOREIGN KEY([librarySubscriptionId])
REFERENCES [CMS].[LibrarySubscriptions] ([id])

ALTER TABLE [CMS].[LibraryPermissions] CHECK CONSTRAINT [FK_LibraryPermissions_LibrarySubscriptions_librarySubscriptionId]

ALTER TABLE [CMS].[LibraryPermissions]  WITH CHECK ADD  CONSTRAINT [FK_LibraryPermissions_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [Accounts].[Users] ([id])

ALTER TABLE [CMS].[LibraryPermissions] CHECK CONSTRAINT [FK_LibraryPermissions_Users_addedById]

ALTER TABLE [CMS].[LibraryPermissions]  WITH CHECK ADD  CONSTRAINT [FK_LibraryPermissions_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [Accounts].[Users] ([id])

ALTER TABLE [CMS].[LibraryPermissions] CHECK CONSTRAINT [FK_LibraryPermissions_Users_updatedById]

ALTER TABLE [CMS].[LibraryPermissions]  WITH CHECK ADD  CONSTRAINT [FK_LibraryPermissions_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[LibraryPermissions] CHECK CONSTRAINT [FK_LibraryPermissions_Refreshed_refreshedId]

/*** Alter LibrarySubscriptions ***/
ALTER TABLE [CMS].[LibrarySubscriptions]  WITH CHECK ADD  CONSTRAINT [FK_LibrarySubscriptions_Libraries_LibraryId] FOREIGN KEY([LibraryId])
REFERENCES [CMS].[Libraries] ([Id])
ON DELETE CASCADE

ALTER TABLE [CMS].[LibrarySubscriptions] CHECK CONSTRAINT [FK_LibrarySubscriptions_Libraries_LibraryId]

ALTER TABLE [CMS].[LibrarySubscriptions]  WITH CHECK ADD  CONSTRAINT [FK_LibrarySubscriptions_Users_SubscribedById] FOREIGN KEY([SubscribedById])
REFERENCES [Accounts].[Users] ([Id])

ALTER TABLE [CMS].[LibrarySubscriptions] CHECK CONSTRAINT [FK_LibrarySubscriptions_Users_SubscribedById]

/*** Alter SavedSearchContentSources ***/
ALTER TABLE [CMS].[SavedSearchContentSources]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchContentSources_SavedSearches_savedSearchId] FOREIGN KEY([savedSearchId])
REFERENCES [CMS].[SavedSearches] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[SavedSearchContentSources] CHECK CONSTRAINT [FK_SavedSearchContentSources_SavedSearches_savedSearchId]

ALTER TABLE [CMS].[SavedSearchContentSources]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchContentSources_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[SavedSearchContentSources] CHECK CONSTRAINT [FK_SavedSearchContentSources_Refreshed_refreshedId]

/*** Alter SavedSearches ***/
ALTER TABLE [CMS].[SavedSearches]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearches_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [Accounts].[Users] ([id])

ALTER TABLE [CMS].[SavedSearches] CHECK CONSTRAINT [FK_SavedSearches_Users_addedById]

ALTER TABLE [CMS].[SavedSearches]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearches_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [Accounts].[Users] ([id])

ALTER TABLE [CMS].[SavedSearches] CHECK CONSTRAINT [FK_SavedSearches_Users_updatedById]

ALTER TABLE [CMS].[SavedSearches]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearches_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[SavedSearches] CHECK CONSTRAINT [FK_SavedSearches_Refreshed_refreshedId]

/*** Alter SavedSearchLibraries ***/
ALTER TABLE [CMS].[SavedSearchLibraries]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchLibraries_Libraries_libraryId] FOREIGN KEY([libraryId])
REFERENCES [CMS].[Libraries] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[SavedSearchLibraries] CHECK CONSTRAINT [FK_SavedSearchLibraries_Libraries_libraryId]

ALTER TABLE [CMS].[SavedSearchLibraries]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchLibraries_SavedSearches_savedSearchId] FOREIGN KEY([savedSearchId])
REFERENCES [CMS].[SavedSearches] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[SavedSearchLibraries] CHECK CONSTRAINT [FK_SavedSearchLibraries_SavedSearches_savedSearchId]

ALTER TABLE [CMS].[SavedSearchLibraries]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchLibraries_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[SavedSearchLibraries] CHECK CONSTRAINT [FK_SavedSearchLibraries_Refreshed_refreshedId]

/*** Alter SavedSearchPermissions ***/
ALTER TABLE [CMS].[SavedSearchPermissions]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchPermissions_SavedSearches_savedSearchId] FOREIGN KEY([savedSearchId])
REFERENCES [CMS].[SavedSearches] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[SavedSearchPermissions] CHECK CONSTRAINT [FK_SavedSearchPermissions_SavedSearches_savedSearchId]

ALTER TABLE [CMS].[SavedSearchPermissions]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchPermissions_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [Accounts].[Users] ([id])

ALTER TABLE [CMS].[SavedSearchPermissions] CHECK CONSTRAINT [FK_SavedSearchPermissions_Users_addedById]

ALTER TABLE [CMS].[SavedSearchPermissions]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchPermissions_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [Accounts].[Users] ([id])

ALTER TABLE [CMS].[SavedSearchPermissions] CHECK CONSTRAINT [FK_SavedSearchPermissions_Users_updatedById]

ALTER TABLE [CMS].[SavedSearchPermissions]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchPermissions_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[SavedSearchPermissions] CHECK CONSTRAINT [FK_SavedSearchPermissions_Refreshed_refreshedId]

/*** Alter SavedSearchCategories ***/
ALTER TABLE [CMS].[SavedSearchCategories]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchCategories_SavedSearches_savedSearchId] FOREIGN KEY([savedSearchId])
REFERENCES [CMS].[SavedSearches] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[SavedSearchCategories] CHECK CONSTRAINT [FK_SavedSearchCategories_SavedSearches_savedSearchId]

ALTER TABLE [CMS].[SavedSearchCategories]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchCategories_Categories_categoryId] FOREIGN KEY([categoryId])
REFERENCES [CMS].[Categories] ([id])

ALTER TABLE [CMS].[SavedSearchCategories] CHECK CONSTRAINT [FK_SavedSearchCategories_Categories_categoryId]

ALTER TABLE [CMS].[SavedSearchCategories]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchCategories_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[SavedSearchCategories] CHECK CONSTRAINT [FK_SavedSearchCategories_Refreshed_refreshedId]

/*** Alter SavedSearchTags ***/
ALTER TABLE [CMS].[SavedSearchTags]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchTags_SavedSearches_savedSearchId] FOREIGN KEY([savedSearchId])
REFERENCES [CMS].[SavedSearches] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[SavedSearchTags] CHECK CONSTRAINT [FK_SavedSearchTags_SavedSearches_savedSearchId]

ALTER TABLE [CMS].[SavedSearchTags]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchTags_Tags_tagId] FOREIGN KEY([tagId])
REFERENCES [CMS].[Tags] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[SavedSearchTags] CHECK CONSTRAINT [FK_SavedSearchTags_Tags_tagId]

ALTER TABLE [CMS].[SavedSearchTags]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchTags_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[SavedSearchTags] CHECK CONSTRAINT [FK_SavedSearchTags_Refreshed_refreshedId]

/*** Alter SearchContentSources ***/
ALTER TABLE [CMS].[SearchContentSources]  WITH CHECK ADD  CONSTRAINT [FK_SearchContentSources_Searches_searchId] FOREIGN KEY([searchId])
REFERENCES [CMS].[Searches] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[SearchContentSources] CHECK CONSTRAINT [FK_SearchContentSources_Searches_searchId]

ALTER TABLE [CMS].[SearchContentSources]  WITH CHECK ADD  CONSTRAINT [FK_SearchContentSources_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[SearchContentSources] CHECK CONSTRAINT [FK_SearchContentSources_Refreshed_refreshedId]

/*** Alter Searches ***/
ALTER TABLE [CMS].[Searches]  WITH CHECK ADD  CONSTRAINT [FK_Searches_Users_searchedById] FOREIGN KEY([searchedById])
REFERENCES [Accounts].[Users] ([id])

ALTER TABLE [CMS].[Searches] CHECK CONSTRAINT [FK_Searches_Users_searchedById]

ALTER TABLE [CMS].[Searches]  WITH CHECK ADD  CONSTRAINT [FK_Searches_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[Searches] CHECK CONSTRAINT [FK_Searches_Refreshed_refreshedId]

/*** Alter SearchLibraries ***/
ALTER TABLE [CMS].[SearchLibraries]  WITH CHECK ADD  CONSTRAINT [FK_SearchLibraries_Searches_searchId] FOREIGN KEY([searchId])
REFERENCES [CMS].[Searches] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[SearchLibraries] CHECK CONSTRAINT [FK_SearchLibraries_Searches_searchId]

ALTER TABLE [CMS].[SearchLibraries]  WITH CHECK ADD  CONSTRAINT [FK_SearchLibraries_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[SearchLibraries] CHECK CONSTRAINT [FK_SearchLibraries_Refreshed_refreshedId]

/*** Alter SearchResults ***/
ALTER TABLE [CMS].[SearchResults]  WITH CHECK ADD  CONSTRAINT [FK_SearchResults_Searches_searchId] FOREIGN KEY([searchId])
REFERENCES [CMS].[Searches] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[SearchResults] CHECK CONSTRAINT [FK_SearchResults_Searches_searchId]

ALTER TABLE [CMS].[SearchResults]  WITH CHECK ADD  CONSTRAINT [FK_SearchResults_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[SearchResults] CHECK CONSTRAINT [FK_SearchResults_Refreshed_refreshedId]

/*** Alter SearchCategories ***/
ALTER TABLE [CMS].[SearchCategories]  WITH CHECK ADD  CONSTRAINT [FK_SearchCategories_Searches_searchId] FOREIGN KEY([searchId])
REFERENCES [CMS].[Searches] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[SearchCategories] CHECK CONSTRAINT [FK_SearchCategories_Searches_searchId]

ALTER TABLE [CMS].[SearchCategories]  WITH CHECK ADD  CONSTRAINT [FK_SearchCategories_Categories_categoryId] FOREIGN KEY([categoryId])
REFERENCES [CMS].[Categories] ([id])

ALTER TABLE [CMS].[SearchCategories] CHECK CONSTRAINT [FK_SearchCategories_Categories_categoryId]

ALTER TABLE [CMS].[SearchCategories]  WITH CHECK ADD  CONSTRAINT [FK_SearchCategories_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[SearchCategories] CHECK CONSTRAINT [FK_SearchCategories_Refreshed_refreshedId]

/*** Alter SearchTags ***/
ALTER TABLE [CMS].[SearchTags]  WITH CHECK ADD  CONSTRAINT [FK_SearchTags_Searches_searchId] FOREIGN KEY([searchId])
REFERENCES [CMS].[Searches] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[SearchTags] CHECK CONSTRAINT [FK_SearchTags_Searches_searchId]

ALTER TABLE [CMS].[SearchTags]  WITH CHECK ADD  CONSTRAINT [FK_SearchTags_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[SearchTags] CHECK CONSTRAINT [FK_SearchTags_Refreshed_refreshedId]

/*** Alter Tags ***/
ALTER TABLE [CMS].[Tags]  WITH CHECK ADD  CONSTRAINT [FK_Tags_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [Accounts].[Users] ([id])

ALTER TABLE [CMS].[Tags] CHECK CONSTRAINT [FK_Tags_Users_addedById]

ALTER TABLE [CMS].[Tags]  WITH CHECK ADD  CONSTRAINT [FK_Tags_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [Accounts].[Users] ([id])

ALTER TABLE [CMS].[Tags] CHECK CONSTRAINT [FK_Tags_Users_updatedById]

ALTER TABLE [CMS].[Tags]  WITH CHECK ADD  CONSTRAINT [FK_Tags_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[Tags] CHECK CONSTRAINT [FK_Tags_Refreshed_refreshedId]

/*** Alter UserFavoriteContents ***/
ALTER TABLE [CMS].[UserFavoriteContents]  WITH CHECK ADD  CONSTRAINT [FK_UserFavoriteContents_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [CMS].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[UserFavoriteContents] CHECK CONSTRAINT [FK_UserFavoriteContents_Contents_contentId]

ALTER TABLE [CMS].[UserFavoriteContents]  WITH CHECK ADD  CONSTRAINT [FK_UserFavoriteContents_Users_userId] FOREIGN KEY([userId])
REFERENCES [Accounts].[Users] ([id])
ON DELETE CASCADE

ALTER TABLE [CMS].[UserFavoriteContents] CHECK CONSTRAINT [FK_UserFavoriteContents_Users_userId]

ALTER TABLE [CMS].[UserFavoriteContents]  WITH CHECK ADD  CONSTRAINT [FK_UserFavoriteContents_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [CMS].[UserFavoriteContents] CHECK CONSTRAINT [FK_UserFavoriteContents_Refreshed_refreshedId]

/*** Alter Users ***/
ALTER TABLE [Accounts].[Users]  WITH CHECK ADD  CONSTRAINT [FK_Users_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [Accounts].[Users] CHECK CONSTRAINT [FK_Users_Refreshed_refreshedId]

/*** Alter Groups ***/
ALTER TABLE [Accounts].[Groups]  WITH CHECK ADD  CONSTRAINT [FK_Groups_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [Accounts].[Groups] CHECK CONSTRAINT [FK_Groups_Refreshed_refreshedId]

/*** Alter GroupMembers ***/
ALTER TABLE [Accounts].[GroupMembers]  WITH CHECK ADD  CONSTRAINT [FK_GroupMembers_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [Core].[Refreshed] ([id])

ALTER TABLE [Accounts].[GroupMembers] CHECK CONSTRAINT [FK_GroupMembers_Refreshed_refreshedId]

ALTER TABLE [Accounts].[GroupMembers]  WITH CHECK ADD  CONSTRAINT [FK_GroupMembers_Users_UserId] FOREIGN KEY([UserId])
REFERENCES [Accounts].[Users] ([id])

ALTER TABLE [Accounts].[GroupMembers] CHECK CONSTRAINT [FK_GroupMembers_Users_UserId]

ALTER TABLE [Accounts].[GroupMembers]  WITH CHECK ADD  CONSTRAINT [FK_GroupMembers_Groups_GroupId] FOREIGN KEY([GroupId])
REFERENCES [Accounts].[Groups] ([id])

ALTER TABLE [Accounts].[GroupMembers] CHECK CONSTRAINT [FK_GroupMembers_Groups_GroupId]