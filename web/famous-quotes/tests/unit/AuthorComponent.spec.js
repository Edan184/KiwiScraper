import { shallowMount } from '@vue/test-utils'
import AuthorComponent from '@/components/AuthorComponent.vue'

describe('AuthorComponent.vue', () => {
    const author = 'Jame Belshey';
    const quotes = [];
  
  it('renders author prop when passed', () => {
    const wrapper = shallowMount(AuthorComponent, {
      props: { author, quotes }
    })
    expect(wrapper.text()).toContain(author);
  });

  it('button text is initally Show when rendered', async () => {
    const wrapper = shallowMount(AuthorComponent, {props: {author, quotes} });
    expect( wrapper.find('button').text()).toBe('Show');
  });

  it('button text changes to when clicked', async () => {
    const wrapper = shallowMount(AuthorComponent, {props: {author, quotes} });
    await wrapper.find('button').trigger('click');
    expect( wrapper.find('button').text()).toBe('Hide');
  })
  
})
