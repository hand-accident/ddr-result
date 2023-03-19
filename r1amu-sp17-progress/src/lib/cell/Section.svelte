<script>
    let className;
    export { className as class };
</script>

<section class="a {className}">
    <slot />
</section>

<style lang="postcss" module>
    .a {
    }
</style>
