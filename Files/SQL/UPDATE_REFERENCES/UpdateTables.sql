
/*** Alter Categories ***/
ALTER TABLE [dbo].[Categories]  WITH CHECK ADD  CONSTRAINT [FK_Categories_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[Categories] CHECK CONSTRAINT [FK_Categories_Refreshed_refreshedId]

/*** Alter Contents ***/
ALTER TABLE [dbo].[Contents]  WITH CHECK ADD  CONSTRAINT [FK_Contents_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[Contents] CHECK CONSTRAINT [FK_Contents_Users_addedById]

ALTER TABLE [dbo].[Contents]  WITH CHECK ADD  CONSTRAINT [FK_Contents_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[Contents] CHECK CONSTRAINT [FK_Contents_Users_updatedById]

ALTER TABLE [dbo].[Contents]  WITH CHECK ADD  CONSTRAINT [FK_Contents_Categories_categoryId] FOREIGN KEY([categoryId])
REFERENCES [dbo].[Categories] ([id])

ALTER TABLE [dbo].[Contents] CHECK CONSTRAINT [FK_Contents_Categories_categoryId]

ALTER TABLE [dbo].[Contents]  WITH CHECK ADD  CONSTRAINT [FK_Contents_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[Contents] CHECK CONSTRAINT [FK_Contents_Refreshed_refreshedId]

/*** Alter ContentAtachments ***/
ALTER TABLE [dbo].[ContentAttachments]  WITH CHECK ADD  CONSTRAINT [FK_ContentAttachments_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [dbo].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[ContentAttachments] CHECK CONSTRAINT [FK_ContentAttachments_Contents_contentId]

ALTER TABLE [dbo].[ContentAttachments]  WITH CHECK ADD  CONSTRAINT [FK_ContentAttachments_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[ContentAttachments] CHECK CONSTRAINT [FK_ContentAttachments_Users_addedById]

ALTER TABLE [dbo].[ContentAttachments]  WITH CHECK ADD  CONSTRAINT [FK_ContentAttachments_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[ContentAttachments] CHECK CONSTRAINT [FK_ContentAttachments_Users_updatedById]

ALTER TABLE [dbo].[ContentAttachments]  WITH CHECK ADD  CONSTRAINT [FK_ContentAttachments_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[ContentAttachments] CHECK CONSTRAINT [FK_ContentAttachments_Refreshed_refreshedId]

/*** Alter ContentDownloads ***/
ALTER TABLE [dbo].[ContentDownloads]  WITH CHECK ADD  CONSTRAINT [FK_ContentDownloads_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [dbo].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[ContentDownloads] CHECK CONSTRAINT [FK_ContentDownloads_Contents_contentId]

ALTER TABLE [dbo].[ContentDownloads]  WITH CHECK ADD  CONSTRAINT [FK_ContentDownloads_Users_downloadedById] FOREIGN KEY([downloadedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[ContentDownloads] CHECK CONSTRAINT [FK_ContentDownloads_Users_downloadedById]

ALTER TABLE [dbo].[ContentDownloads]  WITH CHECK ADD  CONSTRAINT [FK_ContentDownloads_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[ContentDownloads] CHECK CONSTRAINT [FK_ContentDownloads_Refreshed_refreshedId]

/*** Alter ContentFileComponentProperties ***/
ALTER TABLE [dbo].[ContentFileComponentProperties]  WITH CHECK ADD  CONSTRAINT [FK_ContentFileComponentProperties_ContentFileComponents_contentFileComponentId] FOREIGN KEY([contentFileComponentId])
REFERENCES [dbo].[ContentFileComponents] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[ContentFileComponentProperties] CHECK CONSTRAINT [FK_ContentFileComponentProperties_ContentFileComponents_contentFileComponentId]

ALTER TABLE [dbo].[ContentFileComponentProperties]  WITH CHECK ADD  CONSTRAINT [FK_ContentFileComponentProperties_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[ContentFileComponentProperties] CHECK CONSTRAINT [FK_ContentFileComponentProperties_Refreshed_refreshedId]

/*** Alter ContentFileComponents ***/
ALTER TABLE [dbo].[ContentFileComponents]  WITH CHECK ADD  CONSTRAINT [FK_ContentFileComponents_ContentFiles_contentFileId] FOREIGN KEY([contentFileId])
REFERENCES [dbo].[ContentFiles] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[ContentFileComponents] CHECK CONSTRAINT [FK_ContentFileComponents_ContentFiles_contentFileId]

ALTER TABLE [dbo].[ContentFileComponents]  WITH CHECK ADD  CONSTRAINT [FK_ContentFileComponents_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[ContentFileComponents] CHECK CONSTRAINT [FK_ContentFileComponents_Refreshed_refreshedId]

/*** Alter ContentFiles ***/
ALTER TABLE [dbo].[ContentFiles]  WITH CHECK ADD  CONSTRAINT [FK_ContentFiles_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [dbo].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[ContentFiles] CHECK CONSTRAINT [FK_ContentFiles_Contents_contentId]

ALTER TABLE [dbo].[ContentFiles]  WITH CHECK ADD  CONSTRAINT [FK_ContentFiles_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[ContentFiles] CHECK CONSTRAINT [FK_ContentFiles_Users_addedById]

ALTER TABLE [dbo].[ContentFiles]  WITH CHECK ADD  CONSTRAINT [FK_ContentFiles_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[ContentFiles] CHECK CONSTRAINT [FK_ContentFiles_Users_updatedById]

ALTER TABLE [dbo].[ContentFiles]  WITH CHECK ADD  CONSTRAINT [FK_ContentFiles_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[ContentFiles] CHECK CONSTRAINT [FK_ContentFiles_Refreshed_refreshedId]

/*** Alter ContentLibraries ***/
ALTER TABLE [dbo].[ContentLibraries]  WITH CHECK ADD  CONSTRAINT [FK_ContentLibraries_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [dbo].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[ContentLibraries] CHECK CONSTRAINT [FK_ContentLibraries_Contents_contentId]

ALTER TABLE [dbo].[ContentLibraries]  WITH CHECK ADD  CONSTRAINT [FK_ContentLibraries_Libraries_libraryId] FOREIGN KEY([libraryId])
REFERENCES [dbo].[Libraries] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[ContentLibraries] CHECK CONSTRAINT [FK_ContentLibraries_Libraries_libraryId]

ALTER TABLE [dbo].[ContentLibraries]  WITH CHECK ADD  CONSTRAINT [FK_ContentLibraries_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[ContentLibraries] CHECK CONSTRAINT [FK_ContentLibraries_Refreshed_refreshedId]

/*** Alter ContentLoads ***/

ALTER TABLE [dbo].[ContentLoads]  WITH CHECK ADD  CONSTRAINT [FK_ContentLoads_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [dbo].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[ContentLoads] CHECK CONSTRAINT [FK_ContentLoads_Contents_contentId]

ALTER TABLE [dbo].[ContentLoads]  WITH CHECK ADD  CONSTRAINT [FK_ContentLoads_Documents_documentId] FOREIGN KEY([documentId])
REFERENCES [dbo].[Documents] ([id])

ALTER TABLE [dbo].[ContentLoads] CHECK CONSTRAINT [FK_ContentLoads_Documents_documentId]

ALTER TABLE [dbo].[ContentLoads]  WITH CHECK ADD  CONSTRAINT [FK_ContentLoads_Searches_searchId] FOREIGN KEY([searchId])
REFERENCES [dbo].[Searches] ([id])

ALTER TABLE [dbo].[ContentLoads] CHECK CONSTRAINT [FK_ContentLoads_Searches_searchId]

ALTER TABLE [dbo].[ContentLoads]  WITH CHECK ADD  CONSTRAINT [FK_ContentLoads_Users_loadedById] FOREIGN KEY([loadedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[ContentLoads] CHECK CONSTRAINT [FK_ContentLoads_Users_loadedById]

ALTER TABLE [dbo].[ContentLoads]  WITH CHECK ADD  CONSTRAINT [FK_ContentLoads_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[ContentLoads] CHECK CONSTRAINT [FK_ContentLoads_Refreshed_refreshedId]

/*** Alter ContentReviews ***/
ALTER TABLE [dbo].[ContentReviews]  WITH CHECK ADD  CONSTRAINT [FK_ContentReviews_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [dbo].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[ContentReviews] CHECK CONSTRAINT [FK_ContentReviews_Contents_contentId]

ALTER TABLE [dbo].[ContentReviews]  WITH CHECK ADD  CONSTRAINT [FK_ContentReviews_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[ContentReviews] CHECK CONSTRAINT [FK_ContentReviews_Users_addedById]

ALTER TABLE [dbo].[ContentReviews]  WITH CHECK ADD  CONSTRAINT [FK_ContentReviews_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[ContentReviews] CHECK CONSTRAINT [FK_ContentReviews_Users_updatedById]

ALTER TABLE [dbo].[ContentReviews]  WITH CHECK ADD  CONSTRAINT [FK_ContentReviews_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[ContentReviews] CHECK CONSTRAINT [FK_ContentReviews_Refreshed_refreshedId]

/*** Content Revisions ***/
ALTER TABLE [dbo].[ContentRevisions]  WITH CHECK ADD  CONSTRAINT [FK_ContentRevisions_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [dbo].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[ContentRevisions] CHECK CONSTRAINT [FK_ContentRevisions_Contents_contentId]

ALTER TABLE [dbo].[ContentRevisions]  WITH CHECK ADD  CONSTRAINT [FK_ContentRevisions_Users_revisedById] FOREIGN KEY([revisedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[ContentRevisions] CHECK CONSTRAINT [FK_ContentRevisions_Users_revisedById]

ALTER TABLE [dbo].[ContentRevisions]  WITH CHECK ADD  CONSTRAINT [FK_ContentRevisions_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[ContentRevisions] CHECK CONSTRAINT [FK_ContentRevisions_Refreshed_refreshedId]

/*** Alter ContentTags ***/
ALTER TABLE [dbo].[ContentTags]  WITH CHECK ADD  CONSTRAINT [FK_ContentTags_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [dbo].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[ContentTags] CHECK CONSTRAINT [FK_ContentTags_Contents_contentId]

ALTER TABLE [dbo].[ContentTags]  WITH CHECK ADD  CONSTRAINT [FK_ContentTags_Tags_tagId] FOREIGN KEY([tagId])
REFERENCES [dbo].[Tags] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[ContentTags] CHECK CONSTRAINT [FK_ContentTags_Tags_tagId]

ALTER TABLE [dbo].[ContentTags]  WITH CHECK ADD  CONSTRAINT [FK_ContentTags_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[ContentTags] CHECK CONSTRAINT [FK_ContentTags_Refreshed_refreshedId]

/*** Alter Documents (NotNeeded) ***/
ALTER TABLE [dbo].[Documents]  WITH CHECK ADD  CONSTRAINT [FK_Documents_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[Documents] CHECK CONSTRAINT [FK_Documents_Refreshed_refreshedId]

/*** Alter Feedbacks ***/
ALTER TABLE [dbo].[Feedbacks]  WITH CHECK ADD  CONSTRAINT [FK_Feedbacks_Users_submittedById] FOREIGN KEY([submittedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[Feedbacks] CHECK CONSTRAINT [FK_Feedbacks_Users_submittedById]

ALTER TABLE [dbo].[Feedbacks]  WITH CHECK ADD  CONSTRAINT [FK_Feedbacks_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[Feedbacks] CHECK CONSTRAINT [FK_Feedbacks_Refreshed_refreshedId]

/*** Alter Libraries ***/
ALTER TABLE [dbo].[Libraries]  WITH CHECK ADD  CONSTRAINT [FK_Libraries_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[Libraries] CHECK CONSTRAINT [FK_Libraries_Users_addedById]

ALTER TABLE [dbo].[Libraries]  WITH CHECK ADD  CONSTRAINT [FK_Libraries_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[Libraries] CHECK CONSTRAINT [FK_Libraries_Users_updatedById]

ALTER TABLE [dbo].[Libraries]  WITH CHECK ADD  CONSTRAINT [FK_Libraries_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[Libraries] CHECK CONSTRAINT [FK_Libraries_Refreshed_refreshedId]

/*** Alter LibraryPermissions ***/
ALTER TABLE [dbo].[LibraryPermissions]  WITH CHECK ADD  CONSTRAINT [FK_LibraryPermissions_Libraries_libraryId] FOREIGN KEY([libraryId])
REFERENCES [dbo].[Libraries] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[LibraryPermissions] CHECK CONSTRAINT [FK_LibraryPermissions_Libraries_libraryId]

ALTER TABLE [dbo].[LibraryPermissions]  WITH CHECK ADD  CONSTRAINT [FK_LibraryPermissions_LibrarySubscriptions_librarySubscriptionId] FOREIGN KEY([librarySubscriptionId])
REFERENCES [dbo].[LibrarySubscriptions] ([id])

ALTER TABLE [dbo].[LibraryPermissions] CHECK CONSTRAINT [FK_LibraryPermissions_LibrarySubscriptions_librarySubscriptionId]

ALTER TABLE [dbo].[LibraryPermissions]  WITH CHECK ADD  CONSTRAINT [FK_LibraryPermissions_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[LibraryPermissions] CHECK CONSTRAINT [FK_LibraryPermissions_Users_addedById]

ALTER TABLE [dbo].[LibraryPermissions]  WITH CHECK ADD  CONSTRAINT [FK_LibraryPermissions_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[LibraryPermissions] CHECK CONSTRAINT [FK_LibraryPermissions_Users_updatedById]

ALTER TABLE [dbo].[LibraryPermissions]  WITH CHECK ADD  CONSTRAINT [FK_LibraryPermissions_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[LibraryPermissions] CHECK CONSTRAINT [FK_LibraryPermissions_Refreshed_refreshedId]

/*** Alter LibrarySubscriptions ***/
ALTER TABLE [dbo].[LibrarySubscriptions]  WITH CHECK ADD  CONSTRAINT [FK_LibrarySubscriptions_Libraries_LibraryId] FOREIGN KEY([LibraryId])
REFERENCES [dbo].[Libraries] ([Id])
ON DELETE CASCADE

ALTER TABLE [dbo].[LibrarySubscriptions] CHECK CONSTRAINT [FK_LibrarySubscriptions_Libraries_LibraryId]

ALTER TABLE [dbo].[LibrarySubscriptions]  WITH CHECK ADD  CONSTRAINT [FK_LibrarySubscriptions_Users_SubscribedById] FOREIGN KEY([SubscribedById])
REFERENCES [dbo].[Users] ([Id])

ALTER TABLE [dbo].[LibrarySubscriptions] CHECK CONSTRAINT [FK_LibrarySubscriptions_Users_SubscribedById]

/*** Alter SavedSearchContentSources ***/
ALTER TABLE [dbo].[SavedSearchContentSources]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchContentSources_Saved-Searches_savedSearchId] FOREIGN KEY([savedSearchId])
REFERENCES [dbo].[Saved-Searches] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[SavedSearchContentSources] CHECK CONSTRAINT [FK_SavedSearchContentSources_Saved-Searches_savedSearchId]

ALTER TABLE [dbo].[SavedSearchContentSources]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchContentSources_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[SavedSearchContentSources] CHECK CONSTRAINT [FK_SavedSearchContentSources_Refreshed_refreshedId]

/*** Alter Saved-Searches ***/
ALTER TABLE [dbo].[Saved-Searches]  WITH CHECK ADD  CONSTRAINT [FK_Saved-Searches_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[Saved-Searches] CHECK CONSTRAINT [FK_Saved-Searches_Users_addedById]

ALTER TABLE [dbo].[Saved-Searches]  WITH CHECK ADD  CONSTRAINT [FK_Saved-Searches_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[Saved-Searches] CHECK CONSTRAINT [FK_Saved-Searches_Users_updatedById]

ALTER TABLE [dbo].[Saved-Searches]  WITH CHECK ADD  CONSTRAINT [FK_Saved-Searches_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[Saved-Searches] CHECK CONSTRAINT [FK_Saved-Searches_Refreshed_refreshedId]

/*** Alter SavedSearchLibraries ***/
ALTER TABLE [dbo].[SavedSearchLibraries]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchLibraries_Libraries_libraryId] FOREIGN KEY([libraryId])
REFERENCES [dbo].[Libraries] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[SavedSearchLibraries] CHECK CONSTRAINT [FK_SavedSearchLibraries_Libraries_libraryId]

ALTER TABLE [dbo].[SavedSearchLibraries]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchLibraries_Saved-Searches_savedSearchId] FOREIGN KEY([savedSearchId])
REFERENCES [dbo].[Saved-Searches] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[SavedSearchLibraries] CHECK CONSTRAINT [FK_SavedSearchLibraries_Saved-Searches_savedSearchId]

ALTER TABLE [dbo].[SavedSearchLibraries]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchLibraries_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[SavedSearchLibraries] CHECK CONSTRAINT [FK_SavedSearchLibraries_Refreshed_refreshedId]

/*** Alter SavedSearchPermissions ***/
ALTER TABLE [dbo].[SavedSearchPermissions]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchPermissions_Saved-Searches_savedSearchId] FOREIGN KEY([savedSearchId])
REFERENCES [dbo].[Saved-Searches] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[SavedSearchPermissions] CHECK CONSTRAINT [FK_SavedSearchPermissions_Saved-Searches_savedSearchId]

ALTER TABLE [dbo].[SavedSearchPermissions]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchPermissions_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[SavedSearchPermissions] CHECK CONSTRAINT [FK_SavedSearchPermissions_Users_addedById]

ALTER TABLE [dbo].[SavedSearchPermissions]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchPermissions_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[SavedSearchPermissions] CHECK CONSTRAINT [FK_SavedSearchPermissions_Users_updatedById]

ALTER TABLE [dbo].[SavedSearchPermissions]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchPermissions_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[SavedSearchPermissions] CHECK CONSTRAINT [FK_SavedSearchPermissions_Refreshed_refreshedId]

/*** Alter SavedSearchCategories ***/
ALTER TABLE [dbo].[SavedSearchCategories]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchCategories_Saved-Searches_savedSearchId] FOREIGN KEY([savedSearchId])
REFERENCES [dbo].[Saved-Searches] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[SavedSearchCategories] CHECK CONSTRAINT [FK_SavedSearchCategories_Saved-Searches_savedSearchId]

ALTER TABLE [dbo].[SavedSearchCategories]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchCategories_Categories_categoryId] FOREIGN KEY([categoryId])
REFERENCES [dbo].[Categories] ([id])

ALTER TABLE [dbo].[SavedSearchCategories] CHECK CONSTRAINT [FK_SavedSearchCategories_Categories_categoryId]

ALTER TABLE [dbo].[SavedSearchCategories]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchCategories_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[SavedSearchCategories] CHECK CONSTRAINT [FK_SavedSearchCategories_Refreshed_refreshedId]

/*** Alter SavedSearchTags ***/
ALTER TABLE [dbo].[SavedSearchTags]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchTags_Saved-Searches_savedSearchId] FOREIGN KEY([savedSearchId])
REFERENCES [dbo].[Saved-Searches] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[SavedSearchTags] CHECK CONSTRAINT [FK_SavedSearchTags_Saved-Searches_savedSearchId]

ALTER TABLE [dbo].[SavedSearchTags]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchTags_Tags_tagId] FOREIGN KEY([tagId])
REFERENCES [dbo].[Tags] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[SavedSearchTags] CHECK CONSTRAINT [FK_SavedSearchTags_Tags_tagId]

ALTER TABLE [dbo].[SavedSearchTags]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchTags_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[SavedSearchTags] CHECK CONSTRAINT [FK_SavedSearchTags_Refreshed_refreshedId]

/*** Alter SearchContentSources ***/
ALTER TABLE [dbo].[SearchContentSources]  WITH CHECK ADD  CONSTRAINT [FK_SearchContentSources_Searches_searchId] FOREIGN KEY([searchId])
REFERENCES [dbo].[Searches] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[SearchContentSources] CHECK CONSTRAINT [FK_SearchContentSources_Searches_searchId]

ALTER TABLE [dbo].[SearchContentSources]  WITH CHECK ADD  CONSTRAINT [FK_SearchContentSources_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[SearchContentSources] CHECK CONSTRAINT [FK_SearchContentSources_Refreshed_refreshedId]

/*** Alter Searches ***/
ALTER TABLE [dbo].[Searches]  WITH CHECK ADD  CONSTRAINT [FK_Searches_Users_searchedById] FOREIGN KEY([searchedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[Searches] CHECK CONSTRAINT [FK_Searches_Users_searchedById]

ALTER TABLE [dbo].[Searches]  WITH CHECK ADD  CONSTRAINT [FK_Searches_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[Searches] CHECK CONSTRAINT [FK_Searches_Refreshed_refreshedId]

/*** Alter SearchLibraries ***/
ALTER TABLE [dbo].[SearchLibraries]  WITH CHECK ADD  CONSTRAINT [FK_SearchLibraries_Searches_searchId] FOREIGN KEY([searchId])
REFERENCES [dbo].[Searches] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[SearchLibraries] CHECK CONSTRAINT [FK_SearchLibraries_Searches_searchId]

ALTER TABLE [dbo].[SearchLibraries]  WITH CHECK ADD  CONSTRAINT [FK_SearchLibraries_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[SearchLibraries] CHECK CONSTRAINT [FK_SearchLibraries_Refreshed_refreshedId]

/*** Alter SearchResults ***/
ALTER TABLE [dbo].[SearchResults]  WITH CHECK ADD  CONSTRAINT [FK_SearchResults_Searches_searchId] FOREIGN KEY([searchId])
REFERENCES [dbo].[Searches] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[SearchResults] CHECK CONSTRAINT [FK_SearchResults_Searches_searchId]

ALTER TABLE [dbo].[SearchResults]  WITH CHECK ADD  CONSTRAINT [FK_SearchResults_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[SearchResults] CHECK CONSTRAINT [FK_SearchResults_Refreshed_refreshedId]

/*** Alter SearchCategories ***/
ALTER TABLE [dbo].[SearchCategories]  WITH CHECK ADD  CONSTRAINT [FK_SearchCategories_Searches_searchId] FOREIGN KEY([searchId])
REFERENCES [dbo].[Searches] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[SearchCategories] CHECK CONSTRAINT [FK_SearchCategories_Searches_searchId]

ALTER TABLE [dbo].[SearchCategories]  WITH CHECK ADD  CONSTRAINT [FK_SearchCategories_Categories_categoryId] FOREIGN KEY([categoryId])
REFERENCES [dbo].[Categories] ([id])

ALTER TABLE [dbo].[SearchCategories] CHECK CONSTRAINT [FK_SearchCategories_Categories_categoryId]

ALTER TABLE [dbo].[SearchCategories]  WITH CHECK ADD  CONSTRAINT [FK_SearchCategories_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[SearchCategories] CHECK CONSTRAINT [FK_SearchCategories_Refreshed_refreshedId]

/*** Alter SearchTags ***/
ALTER TABLE [dbo].[SearchTags]  WITH CHECK ADD  CONSTRAINT [FK_SearchTags_Searches_searchId] FOREIGN KEY([searchId])
REFERENCES [dbo].[Searches] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[SearchTags] CHECK CONSTRAINT [FK_SearchTags_Searches_searchId]

ALTER TABLE [dbo].[SearchTags]  WITH CHECK ADD  CONSTRAINT [FK_SearchTags_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[SearchTags] CHECK CONSTRAINT [FK_SearchTags_Refreshed_refreshedId]

/*** Alter Tags ***/
ALTER TABLE [dbo].[Tags]  WITH CHECK ADD  CONSTRAINT [FK_Tags_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[Tags] CHECK CONSTRAINT [FK_Tags_Users_addedById]

ALTER TABLE [dbo].[Tags]  WITH CHECK ADD  CONSTRAINT [FK_Tags_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[Tags] CHECK CONSTRAINT [FK_Tags_Users_updatedById]

ALTER TABLE [dbo].[Tags]  WITH CHECK ADD  CONSTRAINT [FK_Tags_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[Tags] CHECK CONSTRAINT [FK_Tags_Refreshed_refreshedId]

/*** Alter UserFavoriteContents ***/
ALTER TABLE [dbo].[UserFavoriteContents]  WITH CHECK ADD  CONSTRAINT [FK_UserFavoriteContents_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [dbo].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[UserFavoriteContents] CHECK CONSTRAINT [FK_UserFavoriteContents_Contents_contentId]

ALTER TABLE [dbo].[UserFavoriteContents]  WITH CHECK ADD  CONSTRAINT [FK_UserFavoriteContents_Users_userId] FOREIGN KEY([userId])
REFERENCES [dbo].[Users] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[UserFavoriteContents] CHECK CONSTRAINT [FK_UserFavoriteContents_Users_userId]

ALTER TABLE [dbo].[UserFavoriteContents]  WITH CHECK ADD  CONSTRAINT [FK_UserFavoriteContents_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[UserFavoriteContents] CHECK CONSTRAINT [FK_UserFavoriteContents_Refreshed_refreshedId]

/*** Alter Users ***/
ALTER TABLE [dbo].[Users]  WITH CHECK ADD  CONSTRAINT [FK_Users_Refreshed_refreshedId] FOREIGN KEY([refreshedId])
REFERENCES [dbo].[Refreshed] ([id])

ALTER TABLE [dbo].[Users] CHECK CONSTRAINT [FK_Users_Refreshed_refreshedId]