# -*- coding: utf-8 -*-
"""
Tureng Dictionary in Flowlauncher.

This plugin allows searching words in Tureng dictionary and opening results in browser.
"""

from flowlauncher import FlowLauncher, FlowLauncherAPI
import urllib.parse
import webbrowser


class TurengSearch(FlowLauncher):

    def query(self, query):
        results = []
        
        try:
            # Get settings from FlowLauncher
            settings = self.rpc_request.get("settings", {})
            # Handle None or empty query
            if query is None:
                query = ""
            
            # Show usage instructions if query is empty
            if not query or len(query.strip()) == 0:
                results.append({
                    "Title": "Search in Tureng",
                    "SubTitle": "Usage: 'tureng word' to search for a word in Tureng dictionary",
                    "IcoPath": "images\\tureng.png",
                    "ContextData": "ctxData"
                })
            else:
                # Remove "tureng" prefix, get only the search word
                search_word = query.strip()
                
                # Validate search word length (prevent extremely long URLs)
                if len(search_word) > 200:
                    results.append({
                        "Title": "Search word too long",
                        "SubTitle": "Please enter a shorter search term (max 200 characters)",
                        "IcoPath": "images\\tureng.png",
                        "ContextData": "ctxData"
                    })
                    return results
                
                # Truncate display word if too long (for UI display)
                display_word = search_word
                if len(display_word) > 50:
                    display_word = display_word[:47] + "..."
                
                # Create URLs for different language pairs
                encoded_word = urllib.parse.quote(search_word, safe='')
                url_tr_en = f"https://tureng.com/tr/turkce-ingilizce/{encoded_word}"
                url_en_tr = f"https://tureng.com/tr/ingilizce-turkce/{encoded_word}"
                url_fr_en = f"https://tureng.com/tr/fransizca-ingilizce/{encoded_word}"
                url_es_en = f"https://tureng.com/tr/ispanyolca-ingilizce/{encoded_word}"
                url_de_en = f"https://tureng.com/tr/almanca-ingilizce/{encoded_word}"
                
                # Validate URL format
                base_urls = [url_tr_en, url_en_tr, url_fr_en, url_es_en, url_de_en]
                if not all(url.startswith("https://tureng.com/") for url in base_urls):
                    raise ValueError("Invalid URL format")
                
                # Get default language from settings, fallback to Turkish-English
                default_lang = settings.get("default_language", "Turkish-English")
                
                # Map language setting to URL
                language_url_map = {
                    "Turkish-English": url_tr_en,
                    "French-English": url_fr_en,
                    "Spanish-English": url_es_en,
                    "German-English": url_de_en
                }
                
                # Get default URL based on settings, fallback to Turkish-English
                default_url = language_url_map.get(default_lang, url_tr_en)
                
                # Display name is the same as the setting value
                default_lang_name = default_lang if default_lang in language_url_map else "Turkish-English"
                
                # Create primary result item with default direction from settings
                results.append({
                    "Title": f"Search \"{display_word}\" in Tureng ({default_lang_name})",
                    "SubTitle": f"Search for \"{display_word}\" in Tureng {default_lang_name} dictionary (Right-click for more options)",
                    "IcoPath": "images\\tureng.png",
                    "ContextData": {
                        "word": search_word,
                        "default_url": default_url,
                        "tr_en_url": url_tr_en,
                        "en_tr_url": url_en_tr,
                        "fr_en_url": url_fr_en,
                        "es_en_url": url_es_en,
                        "de_en_url": url_de_en
                    },
                    "JsonRPCAction": {
                        "method": "open_browser",
                        "parameters": [default_url]
                    }
                })
        
        except Exception as e:
            # Handle any unexpected errors gracefully
            results.append({
                "Title": "Error occurred",
                "SubTitle": "Please try again or check your input",
                "IcoPath": "images\\tureng.png",
                "ContextData": "ctxData"
            })
            # Log error for debugging (FlowLauncher will handle debugMessage)
            self.debug(f"Tureng plugin error: {str(e)}")
        
        return results

    def open_browser(self, url):
        """Open URL in default browser (Tureng or GitHub)."""
        try:
            # Validate URL before opening
            if not url or not isinstance(url, str):
                FlowLauncherAPI.show_msg("Error", "Invalid URL", "images\\tureng.png")
                return
            
            # Allow Tureng and GitHub URLs
            if not (url.startswith("https://tureng.com/") or url.startswith("https://github.com/")):
                FlowLauncherAPI.show_msg("Error", "Invalid URL format", "images\\tureng.png")
                return
            
            # Open browser
            webbrowser.open(url)
        except Exception as e:
            # Handle browser opening errors
            FlowLauncherAPI.show_msg("Error", f"Failed to open browser: {str(e)}", "images\\tureng.png")
    
    def context_menu(self, data):
        """Show context menu with alternative dictionary directions."""
        results = []
        try:
            if not data or not isinstance(data, dict):
                return results
            
            word = data.get("word", "")
            tr_en_url = data.get("tr_en_url", "")
            en_tr_url = data.get("en_tr_url", "")
            fr_en_url = data.get("fr_en_url", "")
            es_en_url = data.get("es_en_url", "")
            de_en_url = data.get("de_en_url", "")
            
            if not word:
                return results
            
            # Truncate display word if too long
            display_word = word
            if len(display_word) > 50:
                display_word = display_word[:47] + "..."
            
            # Add Turkish-English dictionary option
            if tr_en_url and tr_en_url.startswith("https://tureng.com/"):
                results.append({
                    "Title": f"Search \"{display_word}\" in Turkish-English",
                    "SubTitle": "Open Turkish-English dictionary",
                    "IcoPath": "images\\tureng.png",
                    "JsonRPCAction": {
                        "method": "open_browser",
                        "parameters": [tr_en_url]
                    }
                })
            
            # Add French-English dictionary option
            if fr_en_url and fr_en_url.startswith("https://tureng.com/"):
                results.append({
                    "Title": f"Search \"{display_word}\" in French-English",
                    "SubTitle": "Open French-English dictionary",
                    "IcoPath": "images\\tureng.png",
                    "JsonRPCAction": {
                        "method": "open_browser",
                        "parameters": [fr_en_url]
                    }
                })
            
            # Add Spanish-English dictionary option
            if es_en_url and es_en_url.startswith("https://tureng.com/"):
                results.append({
                    "Title": f"Search \"{display_word}\" in Spanish-English",
                    "SubTitle": "Open Spanish-English dictionary",
                    "IcoPath": "images\\tureng.png",
                    "JsonRPCAction": {
                        "method": "open_browser",
                        "parameters": [es_en_url]
                    }
                })
            
            # Add German-English dictionary option
            if de_en_url and de_en_url.startswith("https://tureng.com/"):
                results.append({
                    "Title": f"Search \"{display_word}\" in German-English",
                    "SubTitle": "Open German-English dictionary",
                    "IcoPath": "images\\tureng.png",
                    "JsonRPCAction": {
                        "method": "open_browser",
                        "parameters": [de_en_url]
                    }
                })
            
            # Add separator and author option
            results.append({
                "Title": "Author: Vlamz",
                "SubTitle": "Visit GitHub profile",
                "IcoPath": "images\\tureng.png",
                "JsonRPCAction": {
                    "method": "open_browser",
                    "parameters": ["https://github.com/vlamz"]
                }
            })
        
        except Exception as e:
            # Handle context menu errors gracefully
            self.debug(f"Tureng plugin context menu error: {str(e)}")
        
        return results

