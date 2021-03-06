//------------------------------------------------------------------------------
// Copyright (c) 2012-2013 by European Organization for Nuclear Research (CERN)
// Author: Justin Salmon <jsalmon@cern.ch>
//------------------------------------------------------------------------------
// XRootD is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// XRootD is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public License
// along with XRootD.  If not, see <http://www.gnu.org/licenses/>.
//------------------------------------------------------------------------------

#ifndef UTILS_HH_
#define UTILS_HH_

#include "PyXRootD.hh"

#include "XrdCl/XrdClXRootDResponses.hh"

namespace PyXRootD
{
  //----------------------------------------------------------------------------
  //! Check that the given callback is actually callable.
  //----------------------------------------------------------------------------
  bool IsCallable( PyObject *callable );

  //----------------------------------------------------------------------------
  //! Initialize the Python types for the extension.
  //----------------------------------------------------------------------------
  int InitTypes();

  //----------------------------------------------------------------------------
  //! Check if the given chunk of data contains a newline
  //----------------------------------------------------------------------------
  bool HasNewline( const char *chunk, uint64_t size );

  //----------------------------------------------------------------------------
  //! Split the given string by newlines
  //----------------------------------------------------------------------------
  std::vector<std::string>* SplitNewlines( const char *chunk, uint64_t size );
}

#endif /* UTILS_HH_ */
