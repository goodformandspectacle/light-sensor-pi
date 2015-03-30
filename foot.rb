## Setup

require 'rubygems'
require 'sinatra'
require 'json'

## Controller Actions

get '/' do
  haml :index
end

get '/light' do 
    @@light
end

post '/' do
	@@light = request.body.read
	p request.body.read
end
